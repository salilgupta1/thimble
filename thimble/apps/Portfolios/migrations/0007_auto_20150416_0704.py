# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0006_remove_entry_num_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='cover_photo',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
