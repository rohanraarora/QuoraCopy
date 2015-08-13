# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField(max_length=8192, null=True, blank=True)),
                ('pic', models.ImageField(upload_to='/topics/pics')),
            ],
        ),
    ]
