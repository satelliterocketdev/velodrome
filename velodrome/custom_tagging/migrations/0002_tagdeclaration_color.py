# Generated by Django 2.0.13 on 2021-03-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_tagging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagdeclaration',
            name='color',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
