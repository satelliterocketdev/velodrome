# Generated by Django 2.2.14 on 2021-03-23 20:13

import django.contrib.postgres.fields.jsonb
from django.db import migrations
import velodrome.lock8.models
import velodrome.lock8.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0069_add_explicit_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicyclemodel',
            name='alert_types_to_task',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Mapping of alert types, severity level.\nWhen present, a Task will be created.', validators=[velodrome.lock8.validators.validate_alert_types_to_task]),
        ),
        migrations.AlterField(
            model_name='organizationpreference',
            name='alert_type_to_role_mapping',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='A dictionary in which the keys correspond to Alert types\nand values to Roles. Specified Alert types notify the\ncorresponding Role.', validators=[velodrome.lock8.validators.validate_alert_type_to_role_mapping]),
        ),
        migrations.AlterField(
            model_name='organizationpreference',
            name='allowed_push_alert_types',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=velodrome.lock8.models.get_default_push_alert_types, help_text='List of enabled Alert types\nCorresponds to enabled push notification for each type.', validators=[velodrome.lock8.validators.validate_alert_types]),
        ),
    ]
