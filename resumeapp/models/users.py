# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import validate_email, MinLengthValidator, MaxLengthValidator, RegexValidator

from resume.settings import MIN_VAL_PASS, MAX_VAL_PASS


# Create models Users here.
class User(models.Model):
    '''User's Model'''

    class Meta(object):
        verbose_name = u"Кандидат"
        verbose_name_plural = u"Кандидаты"

    first_name = models.CharField(
        verbose_name=u"Имя",
        max_length=256,
        blank=False
    )

    last_name = models.CharField(
        verbose_name=u"Фамилия",
        max_length=256,
        blank=False
    )

    login = models.CharField(
        verbose_name=u"Логин",
        unique=True,
        max_length=128,
        blank=False,
        default=''
    )

    password = models.CharField(
        verbose_name=u"Пароль",
        max_length=128,
        blank=False,
        validators=[
            MinLengthValidator(MIN_VAL_PASS),
            MaxLengthValidator(MAX_VAL_PASS),
        ],
    )

    email = models.EmailField(
        verbose_name=u"E-mail",
        max_length=75,
        blank=False,
        unique=True,
        validators=[validate_email]
    )

    birthday = models.DateField(
        verbose_name=u"Дата рождения",
        blank=False,
        null=True
    )

    mphone = models.CharField(
        verbose_name=u"Мобильный телефон",
        max_length=75,
        blank=False,
        unique=True,
        validators=[
            RegexValidator(
                regex='^[0-9]{3}\-{1}[0-9]{7}$',
                code=u'Не правильный формат телефона'
            ),
        ]
    )

    photo = models.ImageField(
        verbose_name=u"Аватар",
        blank=True,
        null=True
    )

    experience_summary = models.TextField(
        verbose_name=u"Личный опыт",
        blank=True,
        null=True,
        default=u'',
        help_text=u'Для разделения пуктов используйте ";"'
    )

    technical_skills = models.TextField(
        verbose_name=u"Навыки",
        blank=True,
        null=True,
        default=u'',
        help_text=u'Для разделения пуктов используйте ";"'
    )

    work_experience = models.TextField(
        verbose_name=u"Опыт работы",
        blank=True,
        null=True,
        default=u'',
        help_text=u'Для разделения пуктов используйте ";"'
    )

    education = models.TextField(
        verbose_name=u"Образование",
        blank=True,
        null=True,
        default=u'',
        help_text=u'Для разделения пуктов используйте ";"'
    )

    personal_skills = models.TextField(
        verbose_name=u"Личные качества",
        blank=True,
        null=True,
        default=u'',
        help_text=u'Для разделения пуктов используйте ";"'
    )

    languages = models.TextField(
        verbose_name=u"Языки",
        blank=True,
        null=True,
        default=u'',
        help_text=u'Для разделения пуктов используйте ";"'
    )

    def __unicode__(self):
        new_last_name = self.last_name[0].upper()
        return u"%s %s." % (self.first_name, new_last_name)
