# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0025_university_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='departments',
        ),
        migrations.AddField(
            model_name='lecturer',
            name='department',
            field=models.ForeignKey(blank=True, to='network.Department', null=True),
        ),
    ]
