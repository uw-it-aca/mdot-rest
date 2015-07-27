# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdot_rest', '0004_auto_20150724_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intendedaudience',
            old_name='name',
            new_name='audience',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='resourcelink',
            old_name='title',
            new_name='link_text',
        ),
        migrations.RemoveField(
            model_name='intendedaudience',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='resourcelink',
            name='slug',
        ),
    ]
