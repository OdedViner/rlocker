# Generated by Django 3.1.2 on 2021-03-24 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rqueue', '0006_auto_20210321_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finishedqueue',
            name='pended_time',
        ),
        migrations.AddField(
            model_name='finishedqueue',
            name='pended_time_descriptive',
            field=models.CharField(default=None, max_length=1024, null=True),
        ),
    ]