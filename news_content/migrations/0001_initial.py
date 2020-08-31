# Generated by Django 3.1 on 2020-08-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('short_txt', models.TextField()),
                ('body_txt', models.TextField()),
                ('date', models.CharField(max_length=12)),
                ('time', models.CharField(default='00:00', max_length=12)),
                ('picname', models.TextField()),
            ],
        ),
    ]
