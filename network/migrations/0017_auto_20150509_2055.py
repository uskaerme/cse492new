# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_auto_20150509_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursework',
            name='comments',
            field=models.ManyToManyField(to='network.Comment'),
        ),
        migrations.AddField(
            model_name='submission',
            name='sub_id',
            field=models.CharField(max_length=10, unique=True, null=True),
        ),
    ]
