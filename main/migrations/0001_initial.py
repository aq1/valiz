# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e')),
                ('bio', models.TextField(verbose_name='\u0411\u0438\u043e\u0433\u0440\u0430\u0444\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0412\u0440\u0430\u0447',
                'verbose_name_plural': '\u0412\u0440\u0430\u0447\u0438',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0423\u0441\u043b\u0443\u0433\u0438')),
                ('price', models.CharField(max_length=255, verbose_name='\u0426\u0435\u043d\u0430')),
            ],
            options={
                'verbose_name': '\u0426\u0435\u043d\u0430',
                'verbose_name_plural': '\u0426\u0435\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0430\u0439\u0441 \u041b\u0438\u0441\u0442',
                'verbose_name_plural': '\u041f\u0440\u0430\u0439\u0441 \u041b\u0438\u0441\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.IntegerField(verbose_name='\u0414\u0435\u043d\u044c', choices=[(0, '\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a'), (1, '\u0412\u0442\u043e\u0440\u043d\u0438\u043a'), (2, '\u0421\u0440\u0435\u0434\u0430'), (3, '\u0427\u0435\u0442\u0432\u0435\u0440\u0433'), (4, '\u041f\u044f\u0442\u043d\u0438\u0446\u0430'), (5, '\u0421\u0443\u0431\u0431\u043e\u0442\u0430'), (6, '\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435')])),
                ('parity', models.IntegerField(verbose_name='\u0427\u0435\u0442\u043d\u044b\u0439\\\u041d\u0435\u0447\u0435\u0442\u043d\u044b\u0439', choices=[(0, '\u0427\u0435\u0442\u043d\u044b\u0439'), (1, '\u041d\u0435\u0447\u0435\u0442\u043d\u044b\u0439')])),
                ('begin', models.TimeField(verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e')),
                ('end', models.TimeField(verbose_name='\u041a\u043e\u043d\u0435\u0446')),
                ('doctor', models.ForeignKey(verbose_name='\u0414\u043e\u043a\u0442\u043e\u0440', to='main.Doctor')),
            ],
            options={
                'verbose_name': '\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u0440\u0430\u0447\u0430',
                'verbose_name_plural': '\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u0432\u0440\u0430\u0447\u0430',
            },
        ),
    ]
