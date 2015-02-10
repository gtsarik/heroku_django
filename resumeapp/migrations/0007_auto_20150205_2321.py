# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0006_auto_20150205_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mphone',
            field=models.CharField(unique=True, max_length=75, verbose_name='\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d', validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{3}\\-{1}[0-9]{7}$', code='\u041d\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u0444\u043e\u0440\u043c\u0430\u0442 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430')]),
            preserve_default=True,
        ),
    ]
