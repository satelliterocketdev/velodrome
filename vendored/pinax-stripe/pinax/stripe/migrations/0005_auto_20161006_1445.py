# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-06 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0004_plan_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='country',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]