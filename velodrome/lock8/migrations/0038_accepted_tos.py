# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-13 15:06
from __future__ import unicode_literals

import uuid

import concurrency.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0037_tos'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptedTermsOfService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('concurrency_version', concurrency.fields.IntegerVersionField(default=0, help_text='record revision number')),
                ('terms_of_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepted_terms_of_services', related_query_name='accepted_terms_of_service', to='lock8.TermsOfService')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepted_terms_of_services', related_query_name='accepted_terms_of_service', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='terms_of_services',
            field=models.ManyToManyField(blank=True, related_name='users', related_query_name='user', through='lock8.AcceptedTermsOfService', to='lock8.TermsOfService'),
        ),
        migrations.AlterUniqueTogether(
            name='acceptedtermsofservice',
            unique_together=set([('user', 'terms_of_service')]),
        ),
    ]