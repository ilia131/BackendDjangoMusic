# Generated by Django 4.2.6 on 2024-03-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userartist', '0017_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
    ]
