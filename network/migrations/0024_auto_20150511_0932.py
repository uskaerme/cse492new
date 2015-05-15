# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0023_auto_20150510_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='location',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='academics',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='publications',
        ),
        migrations.RemoveField(
            model_name='student',
            name='academics',
        ),
    ]
