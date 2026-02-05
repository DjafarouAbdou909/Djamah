from django import forms
from .models import Profile
from django.contrib.auth import get_user_model


User = get_user_model()


class UpdateUserForm(forms.ModelForm):
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