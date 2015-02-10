# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0002_auto_20150205_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mphone',
            field=models.CharField(max_length=256, verbose_name='\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d', validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{3}\\-{1}[0-9]{7}$', code='\u041d\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u0444\u043e\u0440\u043c\u0430\u0442 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c', validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(16)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440', blank=True),
            preserve_default=True,
        ),
    ]
