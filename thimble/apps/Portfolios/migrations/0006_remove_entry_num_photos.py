# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0005_auto_20150408_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='num_photos',
        ),
    ]
