# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_auto_20150404_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designer',
            name='designer_id',
        ),
        migrations.AlterField(
            model_name='designer',
            name='user',
            field=models.OneToOneField(primary_key=True, to_field=b'username', serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
