# Generated by Django 2.0.2 on 2018-02-22 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0044_auto_20180219_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='tracking',
        ),
        migrations.RemoveField(
            model_name='bicycle',
            name='latest_gps_tracking',
        ),
        migrations.RemoveField(
            model_name='bicycle',
            name='old_tracking_attributes',
        ),
        migrations.RemoveField(
            model_name='lock',
            name='latest_dss_tracking',
        ),
        migrations.RemoveField(
            model_name='lock',
            name='latest_gps_tracking',
        ),
        migrations.RemoveField(
            model_name='lock',
            name='old_tracking_attributes',
        ),
    ]