# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0007_auto_20150205_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='education',
            field=models.TextField(null=True, verbose_name='\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='experience_summary',
            field=models.TextField(null=True, verbose_name='\u041b\u0438\u0447\u043d\u044b\u0439 \u043e\u043f\u044b\u0442'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.TextField(null=True, verbose_name='\u042f\u0437\u044b\u043a\u0438'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='personal_skills',
            field=models.TextField(null=True, verbose_name='\u041b\u0438\u0447\u043d\u044b\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='technical_skills',
            field=models.TextField(null=True, verbose_name='\u041d\u0430\u0432\u044b\u043a\u0438'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='work_experience',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u044b\u0442 \u0440\u0430\u0431\u043e\u0442\u044b'),
            preserve_default=True,
        ),
    ]
