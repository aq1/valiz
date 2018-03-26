# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180325_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['price_list', 'name', 'price'], 'verbose_name': '\u0426\u0435\u043d\u0430', 'verbose_name_plural': '\u0426\u0435\u043d\u044b'},
        ),
        migrations.AlterModelOptions(
            name='pricelist',
            options={'ordering': ['id'], 'verbose_name': '\u041f\u0440\u0430\u0439\u0441 \u041b\u0438\u0441\u0442', 'verbose_name_plural': '\u041f\u0440\u0430\u0439\u0441 \u041b\u0438\u0441\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='schedule',
            name='parity',
            field=models.IntegerField(default=0, blank=True, verbose_name='\u0427\u0435\u0442\u043d\u044b\u0439\\\u041d\u0435\u0447\u0435\u0442\u043d\u044b\u0439', choices=[(0, '\u0412\u0441\u0435\u0433\u0434\u0430'), (1, '\u041d\u0435\u0447\u0435\u0442'), (2, '\u0427\u0435\u0442')]),
        ),
    ]
