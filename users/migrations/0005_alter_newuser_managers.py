# Generated by Django 5.0.2 on 2024-03-08 18:27

import django.contrib.auth.models
import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_newuser_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='newuser',
            managers=[
                ('new_objects', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
