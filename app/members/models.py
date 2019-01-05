from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.CharField('아이디', max_length=20, unique=True)
    user_pw = models.CharField('비밀번호', max_length=20)
    full_name = models.CharField('이름', max_length=10)
    nickname = models.CharField('별명', max_length=20)
