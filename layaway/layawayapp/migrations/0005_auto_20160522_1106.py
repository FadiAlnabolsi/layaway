# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layawayapp', '0004_auto_20160522_0627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name_plural': 'Artists'},
        ),
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name_plural': 'Event'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name_plural': 'Tickets'},
        ),
        migrations.AlterModelOptions(
            name='ticketinfo',
            options={'verbose_name_plural': 'Ticket Info'},
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
