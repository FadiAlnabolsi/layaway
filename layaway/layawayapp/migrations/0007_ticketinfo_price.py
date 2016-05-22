# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layawayapp', '0006_events_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketinfo',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, default=0),
            preserve_default=False,
        ),
    ]
