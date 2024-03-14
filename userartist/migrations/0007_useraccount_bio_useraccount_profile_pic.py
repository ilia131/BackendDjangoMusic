# Generated by Django 4.2.6 on 2024-02-28 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userartist', '0006_remove_profile_account_profile_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='profile_pic',
            field=models.ImageField(default='avatar.png', upload_to='images/'),
        ),
    ]
