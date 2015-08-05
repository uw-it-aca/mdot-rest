# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdot_rest', '0005_auto_20150724_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcelink',
            name='link_text',
        ),
    ]
