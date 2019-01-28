from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'last_name', 'first_name', 'nickname']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
