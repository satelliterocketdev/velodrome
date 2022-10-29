# Generated by Django 2.0.13 on 2021-01-28 16:57

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lock8', '0063_bicycle_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('read', models.BooleanField(default=True, verbose_name='Readable')),
                ('show', models.BooleanField(default=True, verbose_name='Showable')),
                ('edit', models.BooleanField(default=True, verbose_name='Editable')),
            ],
            options={
                'verbose_name': 'Resource name',
                'db_table': 'features_flags_resources',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RuleAccessModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django.contrib.postgres.fields.jsonb.JSONField(default={}, blank=True, verbose_name='Advanced rules')),
                ('organizations', models.ManyToManyField(db_table='features_flags_org_rules', related_name='features_flags_rules', to='lock8.Organization')),
            ],
            options={
                'verbose_name': 'Access rule',
                'db_table': 'features_flags_access_rules',
                'ordering': ['-template__name'],
            },
        ),
        migrations.CreateModel(
            name='RuleTemplateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('content', django.contrib.postgres.fields.jsonb.JSONField(default={}, verbose_name='Rules')),
            ],
            options={
                'verbose_name': 'Rule template',
                'db_table': 'features_flags_tpl_rules',
                'ordering': ['name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='ruletemplatemodel',
            unique_together={('name',)},
        ),
        migrations.AddField(
            model_name='ruleaccessmodel',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features_flags.RuleTemplateModel', verbose_name='Template'),
        ),
        migrations.AlterUniqueTogether(
            name='resourcemodel',
            unique_together={('name',)},
        ),
    ]