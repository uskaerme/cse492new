# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20150503_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='attachment',
            field=models.FileField(null=True, upload_to=b'attachments', blank=True),
        ),
    ]
