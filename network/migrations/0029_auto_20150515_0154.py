# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0028_auto_20150511_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentContainer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cont_id', models.CharField(max_length=10, unique=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='container',
            field=models.ForeignKey(blank=True, to='network.CommentContainer', null=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='container',
            field=models.ForeignKey(blank=True, to='network.CommentContainer', null=True),
        ),
    ]
