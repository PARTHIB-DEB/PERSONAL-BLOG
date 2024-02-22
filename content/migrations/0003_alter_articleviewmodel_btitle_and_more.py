# Generated by Django 5.0.2 on 2024-02-21 14:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleviewmodel',
            name='btitle',
            field=models.ForeignKey(db_column='title', on_delete=django.db.models.deletion.CASCADE, to='content.articlecreatemodel'),
        ),
        migrations.AlterField(
            model_name='articleviewmodel',
            name='username',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]