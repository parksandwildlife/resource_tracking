# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-04 03:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0028_auto_20170704_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='callsign_display',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Callsign'),
        ),
        migrations.AlterField(
            model_name='device',
            name='callsign',
            field=models.CharField(blank=True, help_text='e.g. 99 for Heavy Duty, Gang Truck or Plant, or free text for other devices', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='rin_number',
            field=models.PositiveIntegerField(blank=True, help_text='Heavy Duty, Gang Truck or Plant only (HD/GT/P automatically prefixed).', null=True, validators=[django.core.validators.MaxValueValidator(999)], verbose_name='Resource Identification Number (RIN)'),
        ),
    ]
