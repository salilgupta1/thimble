# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20150220_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designer',
            name='prof_pic',
            field=cloudinary.models.CloudinaryField(max_length=100, verbose_name=b'image'),
            preserve_default=True,
        ),
    ]
