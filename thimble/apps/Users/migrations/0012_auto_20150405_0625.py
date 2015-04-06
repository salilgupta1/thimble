# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_auto_20150404_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer',
            name='followers',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designer',
            name='following',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
