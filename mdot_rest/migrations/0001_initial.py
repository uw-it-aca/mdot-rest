# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('short_desc', models.CharField(max_length=200)),
                ('feature_desc', models.TextField()),
                ('web_url', models.URLField(blank=True)),
                ('iTunes_url', models.URLField(blank=True)),
                ('Google_Play_url', models.URLField(blank=True)),
                ('Windows_Store_url', models.URLField(blank=True)),
                ('support_url', models.URLField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
