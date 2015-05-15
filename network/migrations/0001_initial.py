# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('user_id', models.CharField(max_length=10, unique=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_lecturer', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=280)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=75, null=True, blank=True)),
                ('semester', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('shortname', models.CharField(max_length=15, null=True, blank=True)),
                ('department_slug', models.SlugField(null=True, blank=True)),
                ('website', models.URLField(max_length=50, null=True, blank=True)),
                ('info', models.CharField(max_length=600, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('shortname', models.CharField(max_length=15, null=True, blank=True)),
                ('faculty_slug', models.SlugField(null=True, blank=True)),
                ('website', models.URLField(max_length=50, null=True, blank=True)),
                ('info', models.CharField(max_length=600, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=280)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('feed_id', models.CharField(max_length=10, unique=True, null=True)),
                ('attachment', models.FileField(default=None, null=True, upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('image', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'profile_pics', blank=True)),
                ('website', models.URLField(max_length=50, null=True, blank=True)),
                ('academic_rank', models.CharField(default=b'Associate Professor', max_length=50, choices=[(b'Professor', b'Professor'), (b'Associate Professor', b'Associate Professor'), (b'Assistant Professor', b'Assistant Professor'), (b'Research/Teaching Assistant', b'Research/Teaching Assistant')])),
                ('admin_rank', models.CharField(blank=True, max_length=50, null=True, choices=[(b'Rector', b'Rector'), (b'Vice Rector', b'Vice Rector'), (b'Dean', b'Dean'), (b'Vice Dean', b'Vice Dean'), (b'Deputy Director', b'Deputy Director'), (b'Head of Department', b'Head of Department'), (b'Chair of Academic Programs', b'Chair of Academic Programs')])),
                ('department', models.ForeignKey(to='network.Department')),
                ('faculty', models.ForeignKey(to='network.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_no', models.CharField(max_length=10)),
                ('course', models.ForeignKey(to='network.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('image', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'profile_pics', blank=True)),
                ('website', models.URLField(max_length=50, null=True, blank=True)),
                ('education', models.CharField(default=b'Graduate', max_length=50, choices=[(b'Graduate', b'Graduate'), (b'Undergraduate', b'Undergraduate')])),
                ('department', models.ForeignKey(to='network.Department')),
                ('faculty', models.ForeignKey(to='network.Faculty')),
                ('sections', models.ManyToManyField(to='network.Section')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
                ('shortname', models.CharField(max_length=15, unique=True, null=True, blank=True)),
                ('university_slug', models.SlugField(unique=True, null=True, blank=True)),
                ('website', models.URLField(max_length=50, null=True, blank=True)),
                ('info', models.CharField(max_length=600, null=True, blank=True)),
                ('location', models.CharField(max_length=600, null=True, blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'profile_pics', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(to='network.University'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='sections',
            field=models.ManyToManyField(related_name='lecturer', to='network.Section'),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='university',
            field=models.ForeignKey(to='network.University'),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='user',
            field=models.OneToOneField(related_name='lecturer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feed',
            name='creator',
            field=models.ForeignKey(to='network.Lecturer'),
        ),
        migrations.AddField(
            model_name='feed',
            name='section',
            field=models.ForeignKey(to='network.Section', null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='university',
            field=models.ForeignKey(to='network.University'),
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(to='network.Faculty'),
        ),
        migrations.AddField(
            model_name='department',
            name='university',
            field=models.ForeignKey(to='network.University'),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(to='network.Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(to='network.Faculty'),
        ),
        migrations.AddField(
            model_name='course',
            name='university',
            field=models.ForeignKey(to='network.University'),
        ),
        migrations.AddField(
            model_name='comment',
            name='feed',
            field=models.ForeignKey(to='network.Feed'),
        ),
    ]
