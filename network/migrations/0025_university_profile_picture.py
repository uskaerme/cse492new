# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0024_auto_20150511_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=b'profile_pics', blank=True),
        ),
    ]
