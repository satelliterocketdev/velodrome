# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-09-14 10:47
from __future__ import unicode_literals

import uuid

import concurrency.fields
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import django_fsm

import velodrome.lock8.models


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0012_install_postgresql_extensions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('concurrency_version', concurrency.fields.IntegerVersionField(default=0, help_text='record revision number')),
                ('message', models.TextField(blank=True, default='')),
                ('category', models.CharField(blank=True, choices=[('location_needs_bicycles', 'Location needs bicycles'), ('bicycle_missing', 'Bicycle missing'), ('bicycle_damaged', 'Bicycle damaged')], max_length=25, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('state', django_fsm.FSMField(db_index=True, default='new', max_length=50)),
                ('bicycle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='support_tickets', related_query_name='support_ticket', to='lock8.Bicycle')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='support_tickets', related_query_name='support_ticket', to='lock8.Organization')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
            bases=(velodrome.lock8.models.OrganizationOwnedModelMixin, models.Model, velodrome.lock8.models.NotificationMessageDeleteMixin, velodrome.lock8.models.SendableModelMixin),
        ),
        migrations.AddField(
            model_name='organizationpreference',
            name='send_support_ticket_per_email',
            field=models.BooleanField(default=False),
        ),
    ]
