# Generated by Django 3.1.1 on 2020-09-17 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripLoading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a unique name for the Trip', max_length=200, unique=True)),
                ('buying_price_per_kg', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_weight_bought', models.IntegerField(default=0, help_text='Enter the total weight bought')),
                ('total_buying_price', models.DecimalField(decimal_places=2, default=1, max_digits=8)),
                ('loading_cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('departure_date', models.DateField()),
                ('comment', models.TextField(blank=True, default='Enter comment if any')),
            ],
            options={
                'verbose_name_plural': 'Start Trip Loading Details',
            },
        ),
        migrations.CreateModel(
            name='TripOffloading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_cost', models.DecimalField(decimal_places=2, default=80000, max_digits=8)),
                ('clearance_cost', models.DecimalField(decimal_places=2, default=9000, max_digits=8)),
                ('selling_price_per_kg', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_weight_sold', models.IntegerField(default=0, help_text='Enter the total weight sold')),
                ('total_selling_price', models.DecimalField(decimal_places=2, default=1, max_digits=8)),
                ('offloading_cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('selling_date', models.DateField()),
                ('broker_expenses', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_expenses', models.DecimalField(decimal_places=2, default=1, max_digits=8)),
                ('profit_margin', models.DecimalField(decimal_places=2, default=1, max_digits=8)),
                ('comment', models.TextField(blank=True, default='Enter comment if any')),
                ('trip_loading', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trip_offloading', to='api.triploading')),
            ],
            options={
                'verbose_name_plural': 'End Trip Offloading Details',
            },
        ),
        migrations.RemoveField(
            model_name='offloading',
            name='loading',
        ),
        migrations.RemoveField(
            model_name='offloading',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='tripinfo',
            name='loading',
        ),
        migrations.RemoveField(
            model_name='tripinfo',
            name='offloading',
        ),
        migrations.RemoveField(
            model_name='tripinfo',
            name='trip',
        ),
        migrations.DeleteModel(
            name='Loading',
        ),
        migrations.DeleteModel(
            name='Offloading',
        ),
        migrations.DeleteModel(
            name='Trip',
        ),
        migrations.DeleteModel(
            name='TripInfo',
        ),
    ]