import re

from django import forms
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class Signup_Form(forms.Form):
    username = forms.CharField(max_length=20, label='아이디',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=30, label='비밀번호',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=30, label="비밀번호 확인",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='이메일', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(max_length=15, label='닉네임',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("이미 사용 중인 아이디입니다.")
        elif not re.match(r'^[a-zA-Z0-9]*$', username) or len(username) < 6:
            raise forms.ValidationError('6~20자의 영문 대소문자, 숫자를 입력하세요')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("비밀번호가 다릅니다.")
        elif not re.match(r'^[a-zA-Z0-9@#$%^&]*$', password1) or \
                not re.match(r'^[a-zA-Z0-9@#$%^&]*$', password2) or \
                len(password1) < 6 or \
                len(password2) < 6:
            raise forms.ValidationError('6~30자의 영문 대소문자, 숫자, 특수문자(@#$%^&)를 입력하세요')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("이미 가입한 이메일입니다.")
        return email

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError("이미 사용 중인 닉네임입니다.")
        elif len(nickname) < 2 or \
                not re.match(r'^[a-zA-Z가-힣0-9]*$', nickname):
            raise forms.ValidationError('2~15자의 한글, 영문 대소문자, 숫자를 입력하세요')

        # for char in nickname:
        #     if not (u"\u0030" <= char <= u"\u0039" or \
        #             u"\u0041" <= char <= u"\u005A" or \
        #             u"\u0061" <= char <= u"\u007A" or \
        #             u"\uAC00" <= char <= u"\uD7A3"):
        #         raise forms.ValidationError('사용할 수 없는 닉네임입니다.')
        #
        # if not re.match(r'^[a-zA-Z가-힣0-9]*$', nickname):
        #     raise forms.ValidationError('사용할 수 없는 닉네임입니다.')

        return nickname

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password2')
        email = cleaned_data.get('email')
        nickname = cleaned_data.get('nickname')
        if self.errors:
            pass
        else:
            User.objects.create_user(username=username,
                                     password=password,
                                     email=email,
                                     nickname=nickname,
                                     )
        user = authenticate(username=username, password=password)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='아이디', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("아이디 또는 비밀번호가 틀렸습니다.")
        return user


class InfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            'nickname'
        }