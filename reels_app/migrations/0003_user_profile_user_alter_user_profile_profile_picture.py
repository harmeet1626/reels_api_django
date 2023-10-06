# Generated by Django 4.2.6 on 2023-10-06 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reels_app', '0002_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='Profile_picture',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
