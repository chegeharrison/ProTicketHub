# Generated by Django 4.2.7 on 2023-11-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketHub', '0002_alter_eventdb_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdb',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]
