# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20180819_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=255, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('map', models.CharField(max_length=255, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0434\u043b\u044f \u043a\u0430\u0440\u0442\u044b')),
                ('schedule', models.CharField(max_length=255, verbose_name='\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('city_number', models.CharField(max_length=255, verbose_name='\u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('mobile_phone', models.CharField(max_length=255, verbose_name='\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('email', models.CharField(max_length=255, verbose_name='\u041f\u043e\u0447\u0442\u0430')),
                ('ceo', models.CharField(max_length=255, verbose_name='\u0414\u0438\u0440\u0435\u043a\u0442\u043e\u0440')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442',
                'verbose_name_plural': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b',
            },
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]
