# -*- coding: utf-8 -*-
# Generated by Django 1.11.6.dev20170907100046 on 2017-10-24 10:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0028_on_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='plan',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Plan'),
        ),
    ]