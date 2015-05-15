# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0019_auto_20150510_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='info',
        ),
        migrations.AddField(
            model_name='faculty',
            name='information',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='location',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
