# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['day', 'parity'], 'verbose_name': '\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u0440\u0430\u0447\u0430', 'verbose_name_plural': '\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u0432\u0440\u0430\u0447\u0430'},
        ),
        migrations.AddField(
            model_name='price',
            name='price_list',
            field=models.ForeignKey(default=1, verbose_name='\u041f\u0440\u0430\u0439\u0441 \u041b\u0438\u0441\u0442', to='main.PriceList'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='bio',
            field=models.TextField(default='', verbose_name='\u0411\u0438\u043e\u0433\u0440\u0430\u0444\u0438\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='parity',
            field=models.IntegerField(default=0, blank=True, verbose_name='\u0427\u0435\u0442\u043d\u044b\u0439\\\u041d\u0435\u0447\u0435\u0442\u043d\u044b\u0439', choices=[(0, '\u0412\u0441\u0435\u0433\u0434\u0430'), (1, '\u041d\u0435\u0447\u0435\u0442\u043d\u044b\u0439'), (2, '\u0427\u0435\u0442\u043d\u044b\u0439')]),
        ),
    ]
