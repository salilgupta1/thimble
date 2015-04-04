# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_auto_20150404_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='designer',
            old_name='prof_pic',
            new_name='avatar',
        ),
    ]
