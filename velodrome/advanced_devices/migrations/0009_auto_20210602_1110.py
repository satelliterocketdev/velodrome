# Generated by Django 2.2.14 on 2021-06-02 11:28

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advanced_devices', '0008_fix_fields_defaults'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceTypeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=64, verbose_name='Brand')),
                ('device_type', models.IntegerField(choices=[(1, 'DISPENSER')], verbose_name='Type')),
                ('name', models.CharField(default='', max_length=64, verbose_name='Product name')),
                ('model', models.CharField(max_length=64, verbose_name='Model (or incept date)')),
                ('formula', models.CharField(choices=[('', 'unknown'), ('gel or liquid', 'gel or liquid'), ('gel', 'gel'), ('liquid', 'liquid'), ('foam', 'foam')], default='', max_length=64, verbose_name='Formula')),
                ('amount_dispensed', models.DecimalField(decimal_places=3, default=0, max_digits=12, verbose_name='Amount dispensed')),
                ('reservoir', models.DecimalField(decimal_places=3, default=0, max_digits=12, verbose_name='Size of reservoir')),
                ('attributes', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'verbose_name': 'Advanced devices type',
                'db_table': 'velodrome_adv_device_type',
            },
        ),
        migrations.AlterField(
            model_name='devicemodel',
            name='device_type',
            field=models.IntegerField(choices=[(1, 'DISPENSER')], db_index=True, verbose_name='Device base type/group'),
        ),
        migrations.AddField(
            model_name='devicemodel',
            name='device_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adv_devices', related_query_name='adv_devices', to='advanced_devices.DeviceTypeModel', verbose_name='Model (type)'),
        ),
    ]