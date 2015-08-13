# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='downvotes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='answer_downvotes'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='upvotes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='answer_upvotes'),
        ),
    ]
