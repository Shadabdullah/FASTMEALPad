# Generated by Django 4.2.4 on 2023-08-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='prepaid_postpaid',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Paid', 'Paid')], max_length=10),
        ),
    ]
