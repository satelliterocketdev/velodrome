# Generated by Django 2.0.13 on 2020-06-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0062_add_device_pairing_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicycle',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
