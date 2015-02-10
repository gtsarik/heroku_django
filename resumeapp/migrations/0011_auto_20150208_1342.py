# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0010_auto_20150207_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(help_text='\u0414\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u044b\u0439 \u0444\u043e\u0440\u043c\u0430\u0442 \u0432\u0432\u043e\u0434\u0430                     "\u0413\u0413\u0413\u0413-\u041c\u041c-\u0414\u0414" (2015-01-31)', null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f'),
            preserve_default=True,
        ),
    ]
