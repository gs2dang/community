from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models


def nickname_length_validator(value):
    if len(value) < 2 or len(value) > 15:
        raise forms.ValidationError('2~15 글자를 입력해주세요')


class User(AbstractUser):
    nickname = models.CharField('닉네임', max_length=20, validators=[nickname_length_validator],
                                help_text="2~15 글자를 입력해주세요")
    login_type = models.CharField('로그인 유형', max_length=25, default='local')

