# Generated by Django 2.0.7 on 2018-08-28 11:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0055_auto_20180626_0611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trip',
            options={'managed': settings.IS_TESTER, 'ordering': ('-pk',)},
        ),
        migrations.RemoveField(
            model_name='organizationpreference',
            name='ride_outside_alert_delay',
        ),
        migrations.AlterField(
            model_name='organizationpreference',
            name='tax_percent',
            field=models.DecimalField(blank=True, decimal_places=3, help_text='Tax percentage to apply to subscriptions and charges.', max_digits=5, null=True),
        ),
    ]