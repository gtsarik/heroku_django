# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0013_auto_20150211_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='experience_summary',
            field=models.TextField(default=' ', help_text='\u0414\u043b\u044f \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u0443\u043a\u0442\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 ";"', null=True, verbose_name='\u041b\u0438\u0447\u043d\u044b\u0439 \u043e\u043f\u044b\u0442', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(default=' ', unique=True, max_length=128, verbose_name='\u041b\u043e\u0433\u0438\u043d'),
            preserve_default=True,
        ),
    ]
