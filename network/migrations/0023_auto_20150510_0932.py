# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0022_department_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='degree',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='academic',
            name='field',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='academic',
            name='institution',
            field=models.CharField(max_length=50),
        ),
    ]
