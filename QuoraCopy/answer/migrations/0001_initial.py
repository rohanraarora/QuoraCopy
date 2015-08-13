# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('rich_text', models.TextField(max_length=8192)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('views_count', models.IntegerField(default=0)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_answers')),
                ('downvotes', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, related_name='answer_downvotes')),
                ('on', models.ForeignKey(to='question.Question', related_name='question_answers')),
                ('upvotes', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, related_name='answer_upvotes')),
            ],
        ),
    ]
