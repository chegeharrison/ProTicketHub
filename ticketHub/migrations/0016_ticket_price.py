# Generated by Django 4.2.7 on 2023-11-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketHub', '0015_eventdb_advanced_price_eventdb_currency_symbol_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
