# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdot_rest', '0006_remove_resourcelink_link_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='image',
            field=models.ImageField(null=True, upload_to=b'uploads', blank=True),
        ),
    ]
