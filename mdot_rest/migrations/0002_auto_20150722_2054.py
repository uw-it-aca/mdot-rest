# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdot_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntendedAudience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('slug', models.SlugField(max_length=60)),
                ('feature_desc', models.CharField(max_length=120)),
                ('featured', models.BooleanField(default=False)),
                ('accessible', models.BooleanField(default=False)),
                ('responsive_web', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='resourcelink',
            name='Google_Play_url',
        ),
        migrations.RemoveField(
            model_name='resourcelink',
            name='Windows_Store_url',
        ),
        migrations.RemoveField(
            model_name='resourcelink',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='resourcelink',
            name='feature_desc',
        ),
        migrations.RemoveField(
            model_name='resourcelink',
            name='iTunes_url',
        ),
        migrations.RemoveField(
            model_name='resourcelink',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='resourcelink',
            name='name',
        ),
        migrations.RemoveField(
            model_name='resourcelink',
            name='short_desc',
        ),
        migrations.RemoveField(
            model_name='resourcelink',
            name='support_url',
        ),
        migrations.RemoveField(
            model_name='resourcelink',
            name='web_url',
        ),
        migrations.AddField(
            model_name='resourcelink',
            name='link_type',
            field=models.CharField(default='WEB', max_length=3, choices=[(b'AND', b'Android'), (b'IOS', b'iOS'), (b'WEB', b'Web'), (b'WIP', b'Windows Phone')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourcelink',
            name='slug',
            field=models.SlugField(default='default_slug', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourcelink',
            name='title',
            field=models.CharField(default='default_title', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourcelink',
            name='url',
            field=models.URLField(default='default_url'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='intendedaudience',
            name='resource',
            field=models.ManyToManyField(to='mdot_rest.Resource'),
        ),
        migrations.AddField(
            model_name='resourcelink',
            name='resource',
            field=models.ManyToManyField(to='mdot_rest.Resource'),
        ),
    ]
