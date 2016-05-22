# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layawayapp', '0003_auto_20160521_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='artist',
        ),
        migrations.AddField(
            model_name='events',
            name='artist',
            field=models.ManyToManyField(to='layawayapp.Artist', blank=True, related_name='artist'),
        ),
    ]
