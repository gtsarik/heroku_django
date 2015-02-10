# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0005_auto_20150205_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(default=b'', unique=True, max_length=128, verbose_name='\u041b\u043e\u0433\u0438\u043d'),
            preserve_default=True,
        ),
    ]
