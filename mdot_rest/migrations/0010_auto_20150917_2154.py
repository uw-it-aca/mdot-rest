# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mdot_rest.optimizedpngfield


class Migration(migrations.Migration):

    dependencies = [
        ('mdot_rest', '0008_auto_20150730_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='uwresource',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='uwresource',
            name='image',
            field=mdot_rest.optimizedpngfield.OptimizedPNGImageField(null=True, upload_to=b'uploads', blank=True),
        ),
    ]
