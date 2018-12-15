from django import forms
from .models import Create_post

class New_posts(forms.ModelForm):
    class Meta:
        model = Create_post
        fields = ('subject', 'title', 'description', 'price')


