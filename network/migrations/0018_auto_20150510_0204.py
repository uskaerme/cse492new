# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0017_auto_20150509_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='info',
        ),
        migrations.AddField(
            model_name='university',
            name='contatc_info',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='university',
            name='established',
            field=models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\d{4}$')]),
        ),
        migrations.AddField(
            model_name='university',
            name='general_info',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='location',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
