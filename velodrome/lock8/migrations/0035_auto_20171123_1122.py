# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-11-23 11:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0034_auto_20171123_0854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricingscheme',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created')},
        ),
    ]