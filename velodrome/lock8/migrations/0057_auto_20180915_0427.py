# Generated by Django 2.0.8 on 2018-09-15 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('lock8', '0056_auto_20180828_1124'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='notificationmessage',
            index_together={('content_type', 'object_id')},
        ),
    ]
