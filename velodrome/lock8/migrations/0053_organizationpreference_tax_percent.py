# Generated by Django 2.0.4 on 2018-04-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0052_auto_20180426_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationpreference',
            name='tax_percent',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Tax percentage to apply to subscriptions and charges.', max_digits=4, null=True),
        ),
    ]
