# Generated by Django 2.2.3 on 2019-09-11 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20190912_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sports_events',
            name='fees_amount',
        ),
        migrations.RemoveField(
            model_name='sports_events',
            name='fees_snu',
        ),
        migrations.RemoveField(
            model_name='sports_events',
            name='prize_money',
        ),
        migrations.RemoveField(
            model_name='technical_events',
            name='fees_amount',
        ),
        migrations.RemoveField(
            model_name='technical_events',
            name='fees_snu',
        ),
        migrations.RemoveField(
            model_name='technical_events',
            name='prize_money',
        ),
    ]
