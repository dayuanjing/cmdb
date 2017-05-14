# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdcGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idc_name', models.CharField(max_length=100)),
                ('idc_address', models.CharField(max_length=100)),
                ('idc_phone', models.CharField(max_length=10)),
                ('idc_email', models.EmailField(max_length=254)),
                ('remarks', models.TextField(blank=True)),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=20)),
                ('remarks', models.TextField(blank=True)),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ServerHistoryInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('h_server_ip', models.GenericIPAddressField()),
                ('h_cpu_version', models.CharField(max_length=100)),
                ('h_cpu_count', models.IntegerField()),
                ('h_cpu_cores', models.IntegerField()),
                ('h_cpu_processor', models.IntegerField()),
                ('h_memory', models.FloatField()),
                ('h_disk', models.FloatField()),
                ('h_idc_group', models.CharField(max_length=10)),
                ('h_item_group', models.CharField(max_length=10)),
                ('update_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_ip', models.GenericIPAddressField()),
                ('server_number', models.CharField(max_length=30)),
                ('server_delivery_date', models.DateField()),
                ('server_version', models.CharField(max_length=50)),
                ('cpu_version', models.CharField(max_length=100)),
                ('cpu_count', models.IntegerField()),
                ('cpu_cores', models.IntegerField()),
                ('cpu_processor', models.IntegerField()),
                ('memory', models.FloatField()),
                ('disk', models.FloatField()),
                ('create_time', models.DateTimeField()),
                ('idc_group', models.ForeignKey(to='servers.IdcGroup')),
                ('item_group', models.ForeignKey(to='servers.ItemGroup')),
            ],
        ),
        migrations.AddField(
            model_name='serverhistoryinfo',
            name='server_number',
            field=models.ForeignKey(to='servers.ServerInfo'),
        ),
    ]
