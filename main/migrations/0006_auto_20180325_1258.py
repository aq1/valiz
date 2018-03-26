# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_doctor_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ['type', 'name'], 'verbose_name': '\u0412\u0440\u0430\u0447', 'verbose_name_plural': '\u0412\u0440\u0430\u0447\u0438'},
        ),
        migrations.AddField(
            model_name='doctor',
            name='category',
            field=models.IntegerField(default=0, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', choices=[(0, '\u0412\u044b\u0441\u0448\u0430\u044f'), (1, '\u041f\u0435\u0440\u0432\u0430\u044f'), (2, '\u0412\u0442\u043e\u0440\u0430\u044f')]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='type',
            field=models.IntegerField(default=0, verbose_name='\u0422\u0438\u043f', choices=[(0, '\u0423\u0417\u0418'), (1, '\u0424\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u0434\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430')]),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='doctor',
            field=models.ForeignKey(related_name='schedule', verbose_name='\u0414\u043e\u043a\u0442\u043e\u0440', to='main.Doctor'),
        ),
    ]
