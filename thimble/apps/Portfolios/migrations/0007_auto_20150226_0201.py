# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0006_auto_20150224_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='designstory',
            old_name='subdomain',
            new_name='designer',
        ),
        migrations.AddField(
            model_name='entry',
            name='cover_photo',
            field=cloudinary.models.CloudinaryField(default='hi', max_length=100, verbose_name=b'image'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='designstory',
            unique_together=set([('designer', 'name')]),
        ),
        migrations.RemoveField(
            model_name='designstory',
            name='cover_photo',
        ),
    ]
