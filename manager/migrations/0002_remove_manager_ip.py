# Generated by Django 3.1 on 2020-08-29 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='ip',
        ),
    ]
