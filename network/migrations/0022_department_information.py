# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0021_auto_20150510_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='information',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
