# Generated by Django 4.2.7 on 2023-11-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketHub', '0019_rename_timestamp_payment_payment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]