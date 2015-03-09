# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0007_auto_20150226_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='num_photos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
