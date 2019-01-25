from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField('이름', max_length=10)
    nickname = models.CharField('별명', max_length=20)
