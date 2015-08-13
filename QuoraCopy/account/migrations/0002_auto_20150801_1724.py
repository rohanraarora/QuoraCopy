# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quorauser',
            old_name='following',
            new_name='following_users',
        ),
        migrations.AddField(
            model_name='quorauser',
            name='following_topics',
            field=models.ManyToManyField(related_name='topic_followers', to='topics.Topic'),
        ),
    ]
