# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0026_auto_20150511_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=models.ManyToManyField(related_name='prerequisites_rel_+', null=True, to='network.Course', blank=True),
        ),
    ]
