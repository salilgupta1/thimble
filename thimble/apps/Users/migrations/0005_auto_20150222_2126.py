# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20150221_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designer',
            name='prof_pic',
            field=cloudinary.models.CloudinaryField(default='def', max_length=100, verbose_name=b'image'),
            preserve_default=False,
        ),
    ]
