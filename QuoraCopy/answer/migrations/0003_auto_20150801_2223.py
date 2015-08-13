# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0002_auto_20150801_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='timestamp',
            new_name='pub_time',
        ),
    ]
