from django import forms
from .models import Posts


class PostsForms(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['content', 'published', 'image', 'pdf', 'url']