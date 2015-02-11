# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import hashlib

from ..models.users import User
from resume.settings import SALT_KEY


class PrivateForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name',
            'login', 'password', 'email',
            'birthday', 'mphone', 'photo',
            'experience_summary', 'technical_skills',
            'work_experience', 'education',
            'personal_skills', 'languages',
            )

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(PrivateForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('private',
            kwargs={'pk': kwargs['instance'].id})

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-3 control-label'
        self.helper.field_class = 'col-sm-9'
        self.helper.span_class = 'glyphicon glyphicon-calendar'

        self.helper.add_input(Submit('add_button', u'Изменить', css_class="btn btn-primary"),)
        self.helper.add_input(Submit('cancel_button', u'Отменить изменения', css_class="btn btn-link"),)

        self.fields['password'].widget = forms.PasswordInput()

    def save(self):
        data = self.cleaned_data
        experience_summary = u''
        technical_skills = u''
        work_experience = u''
        education = u''
        personal_skills = u''
        languages = u''
        data['password'] += SALT_KEY
        data['password'] = hashlib.sha224(data['password']).hexdigest()

        first_name = data['first_name']
        last_name = data['last_name'] 
        login = data['login']
        password = data['password']
        email = data['email']
        birthday = data['birthday']
        mphone = data['mphone']
        photo = data['photo']

        # try:
        #     if data['experience_summary']:
        #         experience_summary = data['experience_summary']
        # except Exception:
        #     pass

        # try:
        #     if data['technical_skills']:
        #         technical_skills = data['technical_skills']
        # except Exception:
        #     pass

        # try:
        #     if data['work_experience']:
        #         work_experience = data['work_experience']
        # except Exception:
        #     pass

        # try:
        #     if data['education']:
        #         education = data['education']
        # except Exception:
        #     pass

        # try:
        #     if data['personal_skills']:
        #         personal_skills = data['personal_skills']
        # except Exception:
        #     pass

        # try:
        #     if data['languages']:
        #         languages = data['languages']
        # except Exception:
        #     pass

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            login=login,
            password=password,
            email=email,
            birthday=birthday,
            mphone=mphone,
            photo=photo
            # experience_summary=experience_summary,
            # technical_skills=technical_skills,
            # work_experience=work_experience,
            # education=education,
            # personal_skills=personal_skills,
            # languages=languages
        )
