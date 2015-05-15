# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_academic_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='academics',
            field=models.ManyToManyField(to='network.Academic'),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='publications',
            field=models.ManyToManyField(to='network.Publication'),
        ),
        migrations.AddField(
            model_name='student',
            name='academics',
            field=models.ManyToManyField(to='network.Academic'),
        ),
    ]
