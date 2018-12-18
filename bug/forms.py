from django import forms
from .models import Bug

class New_posts(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('subject', 'title', 'description',
                  'price')

class Bug(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('comment',)


