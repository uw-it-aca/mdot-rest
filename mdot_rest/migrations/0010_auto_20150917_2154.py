# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mdot_rest.optimizedpngfield


class Migration(migrations.Migration):

    dependencies = [
        ('mdot_rest', '0009_auto_20160421_1947.py'),
    ]

    operations = [
        migrations.AddField(
            model_name='uwresource',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
