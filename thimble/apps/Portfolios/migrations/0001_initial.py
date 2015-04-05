# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_auto_20150404_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignStory',
            fields=[
                ('design_story_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('designer', models.ForeignKey(to='Users.Designer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entry_id', models.AutoField(serialize=False, primary_key=True)),
                ('context', models.TextField(blank=True)),
                ('date', models.DateField(blank=True)),
                ('bucket_link', models.CharField(default=b'dummy', max_length=255)),
                ('cover_photo', cloudinary.models.CloudinaryField(max_length=100, verbose_name=b'image')),
                ('num_photos', models.IntegerField(default=0)),
                ('design_story', models.ForeignKey(to='Portfolios.DesignStory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='designstory',
            unique_together=set([('designer', 'name')]),
        ),
    ]
