# Generated by Django 4.2.7 on 2023-11-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketHub', '0010_rename_date_eventdb_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdb',
            name='Time',
            field=models.TimeField(null=True),
        ),
    ]
