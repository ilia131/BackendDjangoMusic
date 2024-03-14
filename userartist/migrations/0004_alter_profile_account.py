# Generated by Django 4.2.6 on 2024-02-28 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userartist', '0003_profile_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
