# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdot_rest', '0002_auto_20150722_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcelink',
            name='resource',
        ),
        migrations.AddField(
            model_name='resourcelink',
            name='resource',
            field=models.ForeignKey(default=1, to='mdot_rest.Resource', on_delete=django.db.models.deletion.CASCADE),
            preserve_default=False,
        ),
    ]
