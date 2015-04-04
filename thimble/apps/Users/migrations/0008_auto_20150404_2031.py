# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_auto_20150223_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designer',
            name='age',
        ),
        migrations.RemoveField(
            model_name='designer',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='designer',
            name='subdomain',
        ),
        migrations.RemoveField(
            model_name='designer',
            name='template_theme',
        ),
        migrations.RemoveField(
            model_name='designer',
            name='text_bio',
        ),
        migrations.AddField(
            model_name='designer',
            name='bio',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='designer',
            name='prof_pic',
            field=cloudinary.models.CloudinaryField(max_length=100, verbose_name=b'image', blank=True),
            preserve_default=True,
        ),
    ]
