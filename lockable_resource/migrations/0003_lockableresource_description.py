# Generated by Django 3.1.2 on 2021-04-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lockable_resource', '0002_auto_20210301_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='lockableresource',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=2048, null=True),
        ),
    ]
