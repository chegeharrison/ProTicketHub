# Generated by Django 4.2.7 on 2023-11-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketHub', '0005_alter_eventdb_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdb',
            name='location',
            field=models.TextField(max_length=100),
        ),
    ]
