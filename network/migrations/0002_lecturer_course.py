# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='course',
            field=models.ManyToManyField(related_name='courses', to='network.Course'),
        ),
    ]
