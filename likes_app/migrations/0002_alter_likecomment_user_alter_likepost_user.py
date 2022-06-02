# Generated by Django 4.0.4 on 2022-06-02 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='likepost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
