from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'user_pw']


class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'user_pw', 'full_name', 'nickname']
