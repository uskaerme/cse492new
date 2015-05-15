# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0018_auto_20150510_0204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='contatc_info',
            new_name='contact_info',
        ),
    ]
