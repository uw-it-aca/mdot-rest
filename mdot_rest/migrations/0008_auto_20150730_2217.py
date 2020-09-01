# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('mdot_rest', '0007_resource_image'),
    ]

    operations = [
        migrations.RenameModel('Resource', 'UWResource'),
        migrations.AlterField(
            model_name='intendedaudience',
            name='resource',
            field=models.ManyToManyField(to='mdot_rest.UWResource'),
        ),
        migrations.AlterField(
            model_name='resourcelink',
            name='resource',
            field=models.ForeignKey(to='mdot_rest.UWResource', on_delete=django.db.models.deletion.CASCADE),
        ),
    ]
