# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20150222_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Title (optional)', blank=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=100, verbose_name=b'image')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
