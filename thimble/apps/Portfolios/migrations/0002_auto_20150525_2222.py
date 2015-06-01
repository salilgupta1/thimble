# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='comments',
            field=models.PositiveIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collection',
            name='likes',
            field=models.PositiveIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
