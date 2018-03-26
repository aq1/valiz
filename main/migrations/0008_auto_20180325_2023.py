# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180325_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='short_title',
            field=models.CharField(default='', max_length=255, verbose_name='\u041a\u043e\u0440\u043e\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='doctor',
            field=models.ForeignKey(verbose_name='\u0414\u043e\u043a\u0442\u043e\u0440', to='main.Doctor'),
        ),
    ]
