from django import forms
from . import models

class createPost(forms.ModelForm):
    class Meta:
        model=models.Post
        fields=['title','body','slug','banner']