# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_auto_20150509_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursework',
            name='attachment',
            field=models.FileField(null=True, upload_to=b'attachments', blank=True),
        ),
    ]
