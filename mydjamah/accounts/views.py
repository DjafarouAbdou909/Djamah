from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .tokens import generateToken
from .forms import UpdateUserForm, UpdateProfileForm


User = get_user_model()

def home(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")

        # Vérifications
        if User.objects.filter(email=email).exists():
            messages.error(request, "Adresse e-mail déjà utilisée.")
            return redirect("signup")

        if password != password1:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect("signup")

        if len(password) < 8:
            messages.error(request, "Mot de passe trop court (minimum 8 caractères).")
            return redirect("signup")

        # Création utilisateur
        user = User.objects.create_user(email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.is_active = False
        user.save()

        messages.success(request, "Compte créé avec succès. Vérifiez votre e-mail pour l’activer.")

        
        send_mail(
            "Bienvenue sur DJAMAH 🎉",
            f"Bienvenue {firstname} {lastname} !\nMerci de rejoindre DJAMAH.",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        current_site = get_current_site(request)
        email_subject = "Activation de votre compte DJAMAH"

        message = render_to_string("emaiilconfirmation.html", {
            "name": firstname,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": generateToken.make_token(user),
        })

        email_message = EmailMessage(
            email_subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
        email_message.send()

        return redirect("signin")

    return render(request, "signup.html")


def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("profile")
            else:
                messages.error(request, "Veuillez activer votre compte via l’e-mail.")
                return redirect("signin")
        else:
            messages.error(request, "Identifiants incorrects.")
            return redirect("signin")

    return render(request, "signin.html")

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profil mis à jour avec succès.")
            return redirect("Profile")

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, "profile.html", context)



def logOut(request):
    logout(request)
    messages.success(request, "Déconnexion réussie. À bientôt sur DJAMAH.")
    return redirect("home")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and generateToken.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Compte activé avec succès 🎉 Vous pouvez vous connecter.")
        return redirect("signin")
    else:
        messages.error(request, "Lien d’activation invalide ou expiré.")
        return redirect("home")
