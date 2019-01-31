from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField(label='ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Password Confirm", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class LoginForm(forms.Form):
    username = forms.CharField(label='ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


