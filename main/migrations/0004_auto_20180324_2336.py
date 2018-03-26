# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_document_documentimage_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentimage',
            name='document',
            field=models.ForeignKey(verbose_name='\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442', to='main.Document'),
        ),
    ]
