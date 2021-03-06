# Generated by Django 3.0.8 on 2020-12-31 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffprofile',
            name='percentage',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='percentage',
        ),
        migrations.AddField(
            model_name='user',
            name='percentage',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
