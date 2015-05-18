# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0015_auto_20150518_2104'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='piece',
            unique_together=set([]),
        ),
    ]
