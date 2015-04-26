# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0007_auto_20150416_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
