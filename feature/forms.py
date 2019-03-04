from django import forms
from .models import Feature, FeatureComment


class New_posts(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('title', 'description',
                  'price')


class Comment_form(forms.ModelForm):
    class Meta:
        model = FeatureComment
        fields = ('comment',)
