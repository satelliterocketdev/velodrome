# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-11-21 13:42
from __future__ import unicode_literals

import uuid

import concurrency.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0032_white-label-users'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanPass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('concurrency_version', concurrency.fields.IntegerVersionField(default=0, help_text='record revision number')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='subscriptionplan',
            name='is_restricted',
            field=models.BooleanField(default=False, help_text='Restricted plans are availabe only to users associated through plan_passes'),
        ),
        migrations.AddField(
            model_name='planpass',
            name='subscription_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_passes', related_query_name='plan_pass', to='lock8.SubscriptionPlan'),
        ),
        migrations.AddField(
            model_name='planpass',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_passes', related_query_name='plan_pass', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='subscription_plans',
            field=models.ManyToManyField(blank=True, related_name='users', related_query_name='user', through='lock8.PlanPass', to='lock8.SubscriptionPlan'),
        ),
        migrations.AlterUniqueTogether(
            name='planpass',
            unique_together=set([('user', 'subscription_plan')]),
        ),
    ]