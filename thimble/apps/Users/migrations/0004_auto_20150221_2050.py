# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20150221_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designer',
            name='prof_pic',
            field=cloudinary.models.CloudinaryField(max_length=100, null=True, verbose_name=b'image', blank=True),
            preserve_default=True,
        ),
    ]
