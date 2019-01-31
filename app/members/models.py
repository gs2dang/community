from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models


def nickname_length_validator(value):
    if len(value) < 3 or len(value) > 20:
        raise forms.ValidationError('3~20 글자를 입력해주세요')


class User(AbstractUser):
    nickname = models.CharField('닉네임', max_length=20, validators=[nickname_length_validator],
                                help_text="3~20 글자를 입력해주세요")
