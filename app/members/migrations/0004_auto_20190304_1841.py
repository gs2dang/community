# Generated by Django 2.1.5 on 2019-03-04 09:41

from django.db import migrations, models
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20190127_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(help_text='3~20 글자를 입력해주세요', max_length=20, validators=[members.models.nickname_length_validator], verbose_name='닉네임'),
        ),
    ]