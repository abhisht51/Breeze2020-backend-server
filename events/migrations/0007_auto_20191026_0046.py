# Generated by Django 2.2.3 on 2019-10-25 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20191025_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultural_events',
            name='category',
            field=models.CharField(help_text='Examples: music,dance', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cultural_events',
            name='club',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cultural_events',
            name='person_of_contact',
            field=models.CharField(help_text='Name of person representative', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cultural_events',
            name='person_of_contactno',
            field=models.CharField(help_text='Contact number of person representative', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cultural_events',
            name='poster',
            field=models.CharField(help_text='name of poster file', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cultural_events',
            name='registration_link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cultural_events',
            name='rules',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cultural_events',
            name='team_size',
            field=models.CharField(help_text='If solo then enter 1 else no. of required team members', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cultural_events',
            name='time_limit',
            field=models.CharField(help_text='Time limit for one performance or event if not then enter null', max_length=100, null=True),
        ),
    ]