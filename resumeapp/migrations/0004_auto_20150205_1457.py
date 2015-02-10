# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0003_auto_20150205_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c', validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(16)]),
            preserve_default=True,
        ),
    ]
