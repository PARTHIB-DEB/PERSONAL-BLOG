# Generated by Django 5.0.2 on 2024-03-23 07:07

import users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_newuser_managers_alter_newuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='newuser',
            managers=[
                ('objects', users.models.newUserManager()),
            ],
        ),
    ]