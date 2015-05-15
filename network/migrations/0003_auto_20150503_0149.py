# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_lecturer_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecturer',
            old_name='course',
            new_name='courses',
        ),
    ]
