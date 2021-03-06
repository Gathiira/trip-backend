# Generated by Django 3.0.8 on 2020-12-31 22:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TripRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('reference_number', models.CharField(max_length=255, unique=True)),
                ('status', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TripShare',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=255)),
                ('profit_share', models.CharField(max_length=255)),
                ('process_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_profit_share', to='trip.TripRequest')),
            ],
            options={
                'verbose_name_plural': 'shares details',
            },
        ),
        migrations.CreateModel(
            name='TripOffloading',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('selling_price_per_kg', models.CharField(max_length=255)),
                ('total_weight_sold', models.CharField(max_length=255)),
                ('total_selling_price', models.CharField(max_length=255)),
                ('offloading_cost', models.CharField(max_length=255)),
                ('selling_date', models.DateField()),
                ('process_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_offloading_details', to='trip.TripRequest')),
            ],
            options={
                'verbose_name_plural': 'offloading details',
            },
        ),
        migrations.CreateModel(
            name='TripLoading',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('buying_price_per_kg', models.CharField(max_length=255)),
                ('total_weight_bought', models.CharField(max_length=255)),
                ('total_buying_price', models.CharField(max_length=255)),
                ('loading_cost', models.CharField(max_length=255)),
                ('departure_date', models.DateField()),
                ('process_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_loading_details', to='trip.TripRequest')),
            ],
            options={
                'verbose_name_plural': 'loading details',
            },
        ),
        migrations.CreateModel(
            name='TripExpense',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transport_cost', models.CharField(max_length=255)),
                ('clearance_cost', models.CharField(max_length=255)),
                ('broker_cost', models.CharField(max_length=255)),
                ('process_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_expense_details', to='trip.TripRequest')),
            ],
            options={
                'verbose_name_plural': 'expense details',
            },
        ),
    ]
