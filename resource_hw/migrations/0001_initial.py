# Generated by Django 3.2 on 2024-08-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResouceHW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dc_name', models.CharField(default=None, max_length=100)),
                ('storage_max', models.IntegerField(default=0)),
                ('cpu_max', models.IntegerField(default=0)),
                ('memory_max', models.IntegerField(default=0)),
                ('storage_used', models.IntegerField(default=0)),
                ('cpu_used', models.IntegerField(default=0)),
                ('memory_used', models.IntegerField(default=0)),
            ],
        ),
    ]