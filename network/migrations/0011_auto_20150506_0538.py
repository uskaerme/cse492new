# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_auto_20150506_0508'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='section',
            unique_together=set([('course', 'section_no')]),
        ),
    ]
