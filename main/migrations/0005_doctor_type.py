# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180324_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='type',
            field=models.IntegerField(default=0, choices=[(0, '\u0423\u0417\u0418'), (1, '\u0424\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u0434\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430')]),
        ),
    ]
