# Generated by Django 2.0.4 on 2018-04-26 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0051_rentalsession_payments_state'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='planpass',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created'), 'verbose_name_plural': 'plan passes'},
        ),
    ]
