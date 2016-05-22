# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layawayapp', '0005_auto_20160522_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='img',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
