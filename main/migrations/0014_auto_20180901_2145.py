# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_price_ordering'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['price_list', 'ordering', 'name', 'price'], 'verbose_name': '\u0426\u0435\u043d\u0430', 'verbose_name_plural': '\u0426\u0435\u043d\u044b'},
        ),
    ]
