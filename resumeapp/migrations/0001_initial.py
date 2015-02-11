# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


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
                ('login', models.CharField(default=' ', unique=True, max_length=128, verbose_name='\u041b\u043e\u0433\u0438\u043d')),
                ('password', models.CharField(max_length=128, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c', validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(16)])),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name='E-mail', validators=[django.core.validators.EmailValidator()])),
                ('birthday', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('mphone', models.CharField(unique=True, max_length=75, verbose_name='\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d', validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{3}\\-{1}[0-9]{7}$', code='\u041d\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u0444\u043e\u0440\u043c\u0430\u0442 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430')])),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440', blank=True)),
                ('experience_summary', models.TextField(default=' ', help_text='\u0414\u043b\u044f \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u0443\u043a\u0442\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 ";"', null=True, verbose_name='\u041b\u0438\u0447\u043d\u044b\u0439 \u043e\u043f\u044b\u0442', blank=True)),
                ('technical_skills', models.TextField(default=' ', help_text='\u0414\u043b\u044f \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u0443\u043a\u0442\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 ";"', null=True, verbose_name='\u041d\u0430\u0432\u044b\u043a\u0438', blank=True)),
                ('work_experience', models.TextField(default=' ', help_text='\u0414\u043b\u044f \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u0443\u043a\u0442\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 ";"', null=True, verbose_name='\u041e\u043f\u044b\u0442 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True)),
                ('education', models.TextField(default=' ', help_text='\u0414\u043b\u044f \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u0443\u043a\u0442\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 ";"', null=True, verbose_name='\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('personal_skills', models.TextField(default=' ', help_text='\u0414\u043b\u044f \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u0443\u043a\u0442\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 ";"', null=True, verbose_name='\u041b\u0438\u0447\u043d\u044b\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430', blank=True)),
                ('languages', models.TextField(default=' ', help_text='\u0414\u043b\u044f \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u0443\u043a\u0442\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 ";"', null=True, verbose_name='\u042f\u0437\u044b\u043a\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442',
                'verbose_name_plural': '\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u044b',
            },
            bases=(models.Model,),
        ),
    ]
