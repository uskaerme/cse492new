# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0014_auto_20150508_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursework',
            name='section',
            field=models.ForeignKey(blank=True, to='network.Section', null=True),
        ),
    ]
