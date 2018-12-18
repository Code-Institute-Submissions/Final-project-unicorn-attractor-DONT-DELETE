from django import forms
from .models import Bug

class New_posts(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'description')

class Bug_comment(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('comment',)


