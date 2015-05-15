# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20150505_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now=True, null=True)),
                ('coursework_id', models.CharField(max_length=10, unique=True, null=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=75)),
                ('submission_type', models.CharField(default=b'Online', max_length=30, choices=[(b'In class', b'In class'), (b'Online', b'Online')])),
                ('deadline', models.DateTimeField()),
                ('attachment', models.FileField(default=None, null=True, upload_to=b'', blank=True)),
                ('section', models.ForeignKey(to='network.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submission_date', models.DateTimeField(auto_now=True, null=True)),
                ('notes', models.CharField(max_length=150, null=True)),
                ('attachment', models.FileField(null=True, upload_to=b'', blank=True)),
                ('grade', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('course_work', models.ForeignKey(to='network.CourseWork')),
                ('submitted_by', models.ForeignKey(to='network.Student')),
            ],
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='academic_rank',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='admin_rank',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
