# Generated by Django 5.0.2 on 2024-02-18 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_movie_movie_art'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='application.genre'),
        ),
    ]
