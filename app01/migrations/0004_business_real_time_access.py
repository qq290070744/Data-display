# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_business_daily_traffic_categories_city_trading_volume_commodity_categories_commodity_subclass_provin'),
    ]

    operations = [
        migrations.CreateModel(
            name='business_real_time_access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('access_count', models.IntegerField()),
                ('time', models.CharField(max_length=100)),
                ('updatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
