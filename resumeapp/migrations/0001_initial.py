# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=256, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('login', models.CharField(max_length=128, verbose_name='\u041b\u043e\u0433\u0438\u043d')),
                ('password', models.CharField(max_length=128, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c')),
                ('email', models.EmailField(max_length=75, verbose_name='E-mail')),
                ('birthday', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('mphone', models.CharField(max_length=256, verbose_name='\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442',
                'verbose_name_plural': '\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u044b',
            },
            bases=(models.Model,),
        ),
    ]
