# Generated by Django 4.2.6 on 2024-03-27 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userartist', '0060_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='authorFollow',
            new_name='authorfollow',
        ),
    ]
