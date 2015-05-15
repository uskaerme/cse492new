# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20150503_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='creator',
            field=models.ForeignKey(blank=True, to='network.Lecturer', null=True),
        ),
    ]
