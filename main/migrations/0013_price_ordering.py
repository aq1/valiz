# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def update_prices(apps, schema_editor):
    Price = apps.get_model('main', 'Price')
    list(map(lambda p: p.save(), Price.objects.all()))


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20180901_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='ordering',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.RunPython(update_prices)
    ]
