# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0009_auto_20150226_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='num_photos',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
