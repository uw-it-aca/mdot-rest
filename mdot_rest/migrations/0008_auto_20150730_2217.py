# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

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
            field=models.ForeignKey(to='mdot_rest.UWResource'),
        ),
    ]
