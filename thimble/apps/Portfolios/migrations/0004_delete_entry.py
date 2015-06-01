# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0003_collection_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
