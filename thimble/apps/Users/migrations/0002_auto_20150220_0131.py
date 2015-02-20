# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer',
            name='subdomain',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='designer',
            name='template_theme',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='designer',
            name='gender',
            field=models.CharField(default=b'M', max_length=2, blank=True, choices=[(b'M', b'Male'), (b'F', b'Female'), ((b'NA',), b'Prefer not to Disclose'), (b'OT', b'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='designer',
            name='prof_pic',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
