# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180324_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('order', models.IntegerField(verbose_name='\u041c\u0435\u0441\u0442\u043e \u0432 \u0441\u043f\u0438\u0441\u043a\u0435')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442',
                'verbose_name_plural': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='DocumentImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('document', models.ForeignKey(verbose_name='\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442', to='main.Doctor')),
            ],
            options={
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'/', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438',
            },
        ),
    ]
