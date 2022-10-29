# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 10:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0027_change_payment_desc_validation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='axalock',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='axa_locks', related_query_name='axa_lock', to='lock8.Organization'),
        ),
        migrations.AlterField(
            model_name='bicycle',
            name='axa_lock',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lock8.AxaLock'),
        ),
        migrations.AlterField(
            model_name='bicycle',
            name='lock',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lock8.Lock'),
        ),
        migrations.AlterField(
            model_name='bicycle',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bicycles', related_query_name='bicycle', to='lock8.Organization'),
        ),
        migrations.AlterField(
            model_name='clientapp',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='lock',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='locks', related_query_name='lock', to='lock8.Organization'),
        ),
        migrations.AlterField(
            model_name='notificationmessage',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='feedback_category_tree',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organization', related_query_name='organization', to='lock8.FeedbackCategory'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='stripe_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pinax_stripe.Account'),
        ),
        migrations.AlterField(
            model_name='pricingscheme',
            name='bicycle_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pricing_schemes', related_query_name='pricing_scheme', to='lock8.BicycleModel'),
        ),
        migrations.AlterField(
            model_name='rentingscheme',
            name='bicycle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='renting_schemes', related_query_name='renting_scheme', to='lock8.Bicycle'),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='bicycle_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscription_plans', related_query_name='subscription_plan', to='lock8.BicycleModel'),
        ),
        migrations.AlterField(
            model_name='supportticket',
            name='bicycle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='support_tickets', related_query_name='support_ticket', to='lock8.Bicycle'),
        ),
        migrations.AlterField(
            model_name='task',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='zone',
            name='preferred_mechanic',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zones', related_query_name='zone', to=settings.AUTH_USER_MODEL),
        ),
    ]