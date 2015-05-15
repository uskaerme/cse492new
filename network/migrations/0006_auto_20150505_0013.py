# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20150504_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='feed',
        ),
        migrations.AddField(
            model_name='feed',
            name='comments',
            field=models.ManyToManyField(to='network.Comment'),
        ),
    ]
