# Generated by Django 4.0.4 on 2022-05-29 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='title',
            new_name='profession',
        ),
        migrations.RemoveField(
            model_name='team',
            name='content',
        ),
        migrations.RemoveField(
            model_name='team',
            name='image',
        ),
        migrations.RemoveField(
            model_name='team',
            name='tag',
        ),
    ]
