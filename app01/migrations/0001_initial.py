# -*- coding: UTF-8 -*-
# Generated by Django 3.0.4 on 2020-04-01 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('机柜', models.CharField(max_length=32)),
                ('IPMI', models.CharField(max_length=32)),
                ('USER', models.CharField(max_length=32)),
                ('PASS', models.CharField(max_length=32)),
            ],
        ),
    ]
