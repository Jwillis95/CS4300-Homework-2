# Generated by Django 4.2.11 on 2025-03-03 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_rename_booking_date_booking_booking_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
    ]
