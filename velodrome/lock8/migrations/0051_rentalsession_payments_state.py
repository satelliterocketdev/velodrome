# Generated by Django 2.0.3 on 2018-03-19 18:24

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('lock8', '0050_auto_20180316_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalsession',
            name='payment_state',
            field=django_fsm.FSMField(db_index=True, default='unknown', max_length=50),
        ),
    ]