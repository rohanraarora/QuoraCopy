# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=128)),
                ('desc', models.TextField(max_length=8192)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('views_count', models.IntegerField(default=0)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='asked_by')),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='question_followers')),
                ('tags', models.ManyToManyField(to='topics.Topic', related_name='tags')),
            ],
        ),
    ]
