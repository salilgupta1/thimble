# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0013_auto_20150405_0639'),
        ('Portfolios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='designstory',
            name='comments',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designstory',
            name='likes',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designstory',
            name='wip',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
