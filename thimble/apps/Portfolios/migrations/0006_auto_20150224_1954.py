# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0005_auto_20150223_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designstory',
            name='cover_photo',
            field=cloudinary.models.CloudinaryField(max_length=100, verbose_name=b'image'),
            preserve_default=True,
        ),
    ]
