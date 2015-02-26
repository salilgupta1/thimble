# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('designer_id', models.AutoField(serialize=False, primary_key=True)),
                ('text_bio', models.TextField()),
                ('prof_pic', models.URLField(blank=True)),
                ('gender', models.CharField(default=b'M', max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female'), ((b'NA',), b'Prefer not to Disclose'), (b'OT', b'Other')])),
                ('age', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('location', models.CharField(max_length=200, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
