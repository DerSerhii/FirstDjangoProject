# Generated by Django 4.0.5 on 2022-06-12 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_userprofile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='url',
        ),
    ]