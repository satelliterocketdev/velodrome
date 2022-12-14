# Generated by Django 2.2.14 on 2021-03-23 20:13

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features_flags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruleaccessmodel',
            name='content',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, verbose_name='Advanced rules'),
        ),
        migrations.AlterField(
            model_name='ruletemplatemodel',
            name='content',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='Rules'),
        ),
    ]
