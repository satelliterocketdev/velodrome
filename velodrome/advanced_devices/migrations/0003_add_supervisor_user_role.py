# Generated by Django 2.0.13 on 2021-04-07 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advanced_devices', '0002_deviceconfigcontentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceconfigcontentmodel',
            name='content',
            field=models.TextField(default='', verbose_name='Content (ini)'),
        ),
    ]
