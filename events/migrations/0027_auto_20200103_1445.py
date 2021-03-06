# Generated by Django 2.2.7 on 2020-01-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_technical_events_form_array'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultural_events',
            name='fees_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='cultural_events',
            name='fees_snu',
            field=models.DecimalField(decimal_places=2, help_text='For SNU only', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='cultural_events',
            name='prize_money',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='technical_events',
            name='fees_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='technical_events',
            name='fees_snu',
            field=models.DecimalField(decimal_places=2, help_text='For SNU only', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='technical_events',
            name='prize_money',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
