# Generated by Django 3.0.8 on 2020-12-31 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripexpense',
            name='total_expense',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
