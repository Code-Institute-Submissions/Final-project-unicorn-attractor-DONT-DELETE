from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateProfile(forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class UpdateImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]



