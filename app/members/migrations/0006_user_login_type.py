# Generated by Django 2.1.7 on 2019-04-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20190313_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_type',
            field=models.CharField(default='local', max_length=25, verbose_name='로그인 유형'),
        ),
    ]