# Generated by Django 2.2.7 on 2020-01-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_auto_20191231_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='technical_events',
            name='form_array',
            field=models.TextField(default=''),
        ),
    ]
