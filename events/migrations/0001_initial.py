# Generated by Django 2.2.3 on 2019-09-11 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultural_Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('category', models.CharField(help_text='Examples: music,dance', max_length=100)),
                ('club', models.CharField(max_length=100)),
                ('rules', models.CharField(max_length=100)),
                ('fees_snu', models.DecimalField(decimal_places=2, help_text='For SNU niggas only', max_digits=4)),
                ('fees_amount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('prize_money', models.DecimalField(decimal_places=2, max_digits=5)),
                ('team_size', models.CharField(help_text='If solo then enter 1 else no. of required team members', max_length=100)),
                ('time_limit', models.CharField(help_text='Time limit for one performance or event if not then enter null', max_length=100)),
                ('registration_link', models.CharField(max_length=200)),
                ('person_of_contact', models.CharField(help_text='Name of person representative', max_length=100)),
                ('person_of_contactno', models.CharField(help_text='Contact number of person representative', max_length=100)),
                ('poster', models.CharField(help_text='name of poster file', max_length=200)),
            ],
            options={
                'db_table': 'Cultural_Events',
            },
        ),
        migrations.CreateModel(
            name='Sports_Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('fees_amount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('rules', models.CharField(max_length=100)),
                ('prize_money', models.DecimalField(decimal_places=2, max_digits=5)),
                ('team_size', models.CharField(help_text='If solo then enter 1 else no. of required team members', max_length=100)),
                ('fees_snu', models.DecimalField(decimal_places=2, help_text='For SNU niggas only', max_digits=4)),
                ('registration_link', models.CharField(max_length=200)),
                ('person_of_contact', models.CharField(help_text='Name of person representative', max_length=100)),
                ('person_of_contactno', models.CharField(help_text='Contact number of person representative', max_length=100)),
                ('poster', models.CharField(help_text='name of poster file', max_length=200)),
            ],
            options={
                'db_table': 'Sports_Events',
            },
        ),
        migrations.CreateModel(
            name='Technical_Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('club', models.CharField(max_length=100)),
                ('rules', models.CharField(max_length=100)),
                ('fees_snu', models.DecimalField(decimal_places=2, help_text='For SNU niggas only', max_digits=4)),
                ('fees_amount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('prize_money', models.DecimalField(decimal_places=2, max_digits=5)),
                ('team_size', models.CharField(help_text='If solo then enter 1 else no. of required team members', max_length=100)),
                ('time_limit', models.CharField(help_text='Time limit for one event if not then enter null', max_length=100)),
                ('registration_link', models.CharField(max_length=200)),
                ('person_of_contact', models.CharField(help_text='Name of person representative', max_length=100)),
                ('person_of_contactno', models.CharField(help_text='Contact number of person representative', max_length=100)),
                ('poster', models.CharField(help_text='name of poster file', max_length=200)),
            ],
            options={
                'db_table': 'Technical_Events',
            },
        ),
    ]