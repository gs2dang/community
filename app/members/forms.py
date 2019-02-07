from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField(label='ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Password Confirm", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("이미 사용 중인 아이디입니다.")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("비밀번호가 다릅니다.")
        return password2

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password2')
        if self.errors:
            pass
        else:
            User.objects.create_user(username=username,
                                     password=password,
                                     first_name=cleaned_data.get('first_name'),
                                     last_name=cleaned_data.get('last_name'),
                                     nickname=cleaned_data.get('nickname'))
        user = authenticate(username=username, password=password)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            raise forms.ValidationError("아이디 또는 비밀번호가 틀렸습니다.")

        return user
