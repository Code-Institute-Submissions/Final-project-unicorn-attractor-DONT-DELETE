from django import forms
from .models import Feature

class New_posts(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('subject', 'title', 'description',
                  'price')

class Feature(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('comment',)


