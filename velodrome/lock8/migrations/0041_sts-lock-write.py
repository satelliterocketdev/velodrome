# Generated by Django 2.0.1 on 2018-01-16 14:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0040_auto_20180112_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientapp',
            name='scopes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('bicycle:read', 'bicycle:read'), ('bicycle:write', 'bicycle:write'), ('lock:write', 'lock:write'), ('organization:read', 'organization:read'), ('trip:read', 'trip:read')], max_length=64), blank=True, default=list, size=None),
        ),
    ]
