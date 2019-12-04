# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_announcement_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='announcements'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='type',
            field=models.IntegerField(verbose_name='Тип', default=0, choices=[(0, 'УЗИ'), (1, 'Функциональная диагностика'), (2, 'Консультация врача кардиолога'), (3, 'Консультация врача невролога'), (4, 'Консультация врача ревматолога')]),
        ),
    ]
