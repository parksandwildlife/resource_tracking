# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0015_auto_20170131_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='other_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='district',
            field=models.CharField(choices=[('SWAN', 'Swan Region'), ('PHD', 'Perth Hills'), ('SCD', 'Swan Coastal'), ('SWR', 'South West Region'), ('BWD', 'Blackwood'), ('WTN', 'Wellington'), ('WR', 'Warren Region'), ('DON', 'Donnelly'), ('FRK', 'Frankland'), ('SCR', 'South Coast Region'), ('ALB', 'Albany'), ('ESP', 'Esperance'), ('KIMB', 'Kimberley Region'), ('EKD', 'East Kimberley'), ('WKD', 'West Kimberley'), ('EXM', 'Exmouth'), ('PIL', 'Pilbara'), ('GLD', 'Kalgoorlie'), ('MWR', 'Midwest Region'), ('GER', 'Geraldton'), ('MOR', 'Moora'), ('SHB', 'Shark Bay'), ('WBR', 'Wheatbelt Region'), ('CWB', 'Central Wheatbelt'), ('SWB', 'Southern Wheatbelt'), ('AV', 'Aviation'), ('OTH', 'Other')], default='OTH', max_length=32, verbose_name='Region/District'),
        ),
    ]
