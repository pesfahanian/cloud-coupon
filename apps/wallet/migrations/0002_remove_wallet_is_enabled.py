# Generated by Django 4.2 on 2023-06-21 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='is_enabled',
        ),
    ]
