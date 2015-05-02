# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0014_auto_20150416_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designer',
            name='bio',
            field=models.TextField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
