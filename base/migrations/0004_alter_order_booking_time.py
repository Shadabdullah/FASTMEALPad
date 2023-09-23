# Generated by Django 4.2.4 on 2023-09-23 03:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_order_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='booking_time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
