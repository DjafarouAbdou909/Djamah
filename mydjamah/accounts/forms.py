from django import forms
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class UpdateUserForm(forms.ModelForm):
    """
    Formulaire de mise à jour des informations de base
    de l'utilisateur (prénom et nom).
    
    - Champs obligatoires
    """

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
    """
    Formulaire de mise à jour du profil utilisateur.

    - Gère l'avatar, la biographie et l'établissement scolaire
    - Support des champs optionnels et obligatoires
    """

    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )

    bio = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5
        })
    )

    ecole = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'ecole']

