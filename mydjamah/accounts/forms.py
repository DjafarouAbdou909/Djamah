from django import forms
from .models import Profile
from django.contrib.auth import get_user_model


# Récupération du modèle User personnalisé
User = get_user_model()


class UpdateUserForm(forms.ModelForm):
    """
    Formulaire de mise à jour des informations de base
    de l'utilisateur (nom et prénom).
    """

    # Champ prénom avec style personnalisé
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    # Champ nom avec style personnalisé
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        # Modèle associé au formulaire
        model = User

        # Champs autorisés à être modifiés
        fields = ['first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
    """
    Formulaire de mise à jour du profil utilisateur
    (photo, bio et établissement scolaire).
    """

    # Champ photo de profil
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )

    # Champ biographie
    bio = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5
        })
    )

    # Champ établissement scolaire
    ecole = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        # Modèle associé au formulaire
        model = Profile

        # Champs autorisés à être modifiés
        fields = ['avatar', 'bio', 'ecole']
