# Generated by Django 4.1.5 on 2023-02-08 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP2', '0013_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
