# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0029_auto_20150515_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='comments',
        ),
    ]
