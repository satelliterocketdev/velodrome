# Generated by Django 2.0.13 on 2021-03-24 11:28

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models

import velodrome.lock8.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0065_zone_thresholds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alert_type',
            field=models.CharField(choices=[('lock.bat.low', 'Low Battery'), ('bicycle.ride_outside', 'Outside Service Area'), ('lock.no_tracking', 'Device Not Reporting'), ('bicycle.return_outside', 'Outside Dropzone'), ('bicycle.lost_reported', 'Lost Bicycle Reported'), ('bicycle.outside_operational_period', 'Bicycle is used outside operational period'), ('bicycle.too_long_idle', 'No Recent Rides'), ('bicycle.left_unlocked', 'Bicycle left unlocked'), ('lock.shutdown', 'Device Shutdown'), ('lock.locked_wo_cable', 'Bicycle was locked without a cable'), ('zone.high_threshold', 'Zone has reached a high threshold'), ('zone.low_threshold', 'Zone has reached a low threshold'), ('bicycle.bike_stolen', 'Bicycle being stolen'), ('lock.alarm_triggered', 'Alarm of lock triggered')], max_length=64),
        ),
        migrations.AlterField(
            model_name='organizationpreference',
            name='allowed_push_alert_types',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=['lock.bat.low', 'bicycle.ride_outside', 'lock.no_tracking', 'bicycle.return_outside', 'bicycle.lost_reported', 'bicycle.outside_operational_period', 'bicycle.too_long_idle', 'bicycle.left_unlocked', 'lock.shutdown', 'lock.locked_wo_cable', 'zone.high_threshold', 'zone.low_threshold', 'bicycle.bike_stolen', 'lock.alarm_triggered'], help_text='List of enabled Alert types\nCorresponds to enabled push notification for each type.', validators=[velodrome.lock8.validators.validate_alert_types]),
        ),
    ]