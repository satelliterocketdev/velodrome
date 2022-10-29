# Generated by Django 2.0.3.dev20180227010029 on 2018-02-28 22:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0046_remove_zone_is_maintenance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientapp',
            name='scopes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('bicycle:read', 'bicycle:read'), ('bicycle:write', 'bicycle:write'), ('lock:write', 'lock:write'), ('organization:read', 'organization:read'), ('trip:read', 'trip:read'), ('zone:read', 'zone:read'), ('zone:write', 'zone:write')], max_length=64), blank=True, default=list, size=None),
        ),
    ]
