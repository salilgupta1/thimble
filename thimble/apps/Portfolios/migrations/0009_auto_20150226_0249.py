# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0008_entry_num_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='bucket_link',
            field=models.CharField(default=b'dummy', max_length=255),
            preserve_default=True,
        ),
    ]
