# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20150505_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.RemoveField(
            model_name='university',
            name='image',
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'profile_pics', blank=True),
        ),
    ]
