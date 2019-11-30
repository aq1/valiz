# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='datetime',
            field=models.DateTimeField(verbose_name='Дата публикации', default=django.utils.timezone.now),
        ),
    ]
