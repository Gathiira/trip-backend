# Generated by Django 3.0.3 on 2020-10-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20201008_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharesmodel',
            name='percentage',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=19),
        ),
    ]
