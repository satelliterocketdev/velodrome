# Generated by Django 2.0.2 on 2018-02-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0042_merge_20180125_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='app_download_url',
            field=models.URLField(blank=True, max_length=254, null=True),
        ),
    ]
