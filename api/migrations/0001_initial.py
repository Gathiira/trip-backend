# Generated by Django 3.0.3 on 2020-09-26 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TripLoading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a unique name for the Trip', max_length=200, unique=True)),
                ('buying_price_per_kg', models.DecimalField(decimal_places=2, default=1, max_digits=19)),
                ('total_weight_bought', models.DecimalField(decimal_places=2, default=1, help_text='Enter the total weight bought', max_digits=19)),
                ('total_buying_price', models.DecimalField(decimal_places=2, default=1, max_digits=19)),
                ('loading_cost', models.DecimalField(decimal_places=2, default=1, max_digits=19)),
                ('departure_date', models.DateField()),
                ('comment', models.TextField(blank=True, default='Enter comment if any')),
            ],
            options={
                'verbose_name_plural': 'Loading Details',
            },
        ),
        migrations.CreateModel(
            name='UserContribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.DecimalField(decimal_places=2, default=1, max_digits=19)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TripOffloading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_cost', models.DecimalField(decimal_places=2, default=80000, max_digits=19)),
                ('clearance_cost', models.DecimalField(decimal_places=2, default=9000, max_digits=19)),
                ('selling_price_per_kg', models.DecimalField(decimal_places=2, max_digits=19)),
                ('total_weight_sold', models.DecimalField(decimal_places=2, default=1, help_text='Enter the total weight sold', max_digits=19)),
                ('total_selling_price', models.DecimalField(decimal_places=2, default=1, max_digits=19)),
                ('offloading_cost', models.DecimalField(decimal_places=2, max_digits=19)),
                ('selling_date', models.DateField()),
                ('broker_expenses', models.DecimalField(decimal_places=2, max_digits=19)),
                ('total_expenses', models.DecimalField(decimal_places=2, default=1, max_digits=19)),
                ('profit_margin', models.DecimalField(decimal_places=2, default=1, max_digits=19)),
                ('comment', models.TextField(blank=True, default='Enter comment if any')),
                ('trip_loading', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trip_offloading', to='api.TripLoading')),
            ],
            options={
                'verbose_name_plural': 'Offloading Details',
            },
        ),
        migrations.CreateModel(
            name='SharesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_capital', models.DecimalField(decimal_places=2, default=1, max_digits=19)),
                ('profit_share', models.DecimalField(decimal_places=2, default=1, max_digits=19)),
                ('contribution', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_contribution', to='api.UserContribution')),
                ('profit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profit', to='api.TripOffloading')),
            ],
        ),
    ]
