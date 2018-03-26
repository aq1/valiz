# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_contacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['order'], 'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442', 'verbose_name_plural': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b'},
        ),
        migrations.AddField(
            model_name='contacts',
            name='map',
            field=models.CharField(default='', max_length=255, verbose_name='\u041a\u0430\u0440\u0442\u0430'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documentimage',
            name='image',
            field=models.ImageField(upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to=b'', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f'),
        ),
    ]
