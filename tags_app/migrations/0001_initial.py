# Generated by Django 4.0.4 on 2022-06-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('first_app', '0003_remove_post_image_post_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('posts', models.ManyToManyField(related_name='tags', to='first_app.post')),
            ],
        ),
    ]
