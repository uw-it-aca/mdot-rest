# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
            field=models.ForeignKey(default='', to='mdot_rest.Resource'),
            preserve_default=False,
        ),
    ]
