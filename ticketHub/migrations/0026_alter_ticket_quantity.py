# Generated by Django 4.2.7 on 2023-11-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketHub', '0025_remove_payment_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
