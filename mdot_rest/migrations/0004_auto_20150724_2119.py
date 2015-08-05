# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdot_rest', '0003_auto_20150723_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='campus_bothell',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resource',
            name='campus_seattle',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resource',
            name='campus_tacoma',
            field=models.BooleanField(default=False),
        ),
    ]
