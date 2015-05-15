# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_auto_20150506_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree', models.CharField(max_length=100)),
                ('field', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(regex=b'^\\d{4}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(regex=b'^\\d{4}$')])),
                ('reference', models.CharField(max_length=250)),
                ('link', models.URLField(max_length=100, null=True, blank=True)),
            ],
        ),
    ]
