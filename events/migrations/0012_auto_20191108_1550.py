# Generated by Django 2.2.3 on 2019-11-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20191030_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultural_events',
            name='form_array',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='event_registrations',
            name='form_array',
            field=models.TextField(default=''),
        ),
    ]
