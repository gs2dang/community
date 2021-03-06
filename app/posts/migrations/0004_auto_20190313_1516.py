# Generated by Django 2.1.5 on 2019-03-13 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190305_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postlike',
            options={'verbose_name': '추천', 'verbose_name_plural': '추천'},
        ),
        migrations.AddField(
            model_name='post',
            name='comment_count',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='댓글수'),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='좋아요 누른 사람'),
        ),
    ]
