# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0020_auto_20150510_0345'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=300)),
                ('time', models.TimeField(blank=True)),
                ('section', models.ForeignKey(to='network.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('start', models.CharField(max_length=50)),
                ('end', models.CharField(max_length=50)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='course',
            name='university',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='department',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='university',
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='student',
            name='university',
        ),
        migrations.AddField(
            model_name='academic',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='feed',
            field=models.ForeignKey(blank=True, to='network.Feed', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='grading',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='info',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisites',
            field=models.ManyToManyField(related_name='prerequisites_rel_+', to='network.Course'),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='departments',
            field=models.ManyToManyField(to='network.Department'),
        ),
        migrations.AddField(
            model_name='publication',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='departments',
            field=models.ManyToManyField(to='network.Department'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='section',
            field=models.ForeignKey(blank=True, to='network.Section', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together=set([('faculty', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='faculty',
            unique_together=set([('university', 'name')]),
        ),
        migrations.RemoveField(
            model_name='department',
            name='info',
        ),
        migrations.RemoveField(
            model_name='department',
            name='university',
        ),
    ]
