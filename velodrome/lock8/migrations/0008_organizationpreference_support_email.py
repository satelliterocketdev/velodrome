# -*- coding: utf-8 -*-
# Generated by Django 1.11.4.dev20170719152621 on 2017-07-19 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0007_auto_20170707_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationpreference',
            name='support_email',
            field=models.EmailField(blank=True, default=None, help_text='Primary support email address.', max_length=254, null=True),
        ),
    ]
