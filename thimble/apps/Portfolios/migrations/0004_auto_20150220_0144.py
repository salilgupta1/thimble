# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0003_auto_20150220_0134'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]
