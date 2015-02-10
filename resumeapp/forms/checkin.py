# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from simplemathcaptcha.fields import MathCaptchaField
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import hashlib

from ..models.users import User
from resume.settings import SALT_KEY


class CheckInForm(ModelForm):
    captcha = MathCaptchaField()
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name',
            'login', 'password', 'email',
            'birthday', 'mphone', 'photo'
            )

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(CheckInForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('checkin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-3 control-label'
        self.helper.field_class = 'col-sm-9'

        # form buttons
        self.helper.add_input(Submit('send_button', u'Зрегистрироваться'))

        self.fields['password'].widget = forms.PasswordInput()

    def save(self):
        data = self.cleaned_data
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

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            login=login,
            password=password,
            email=email,
            birthday=birthday,
            mphone=mphone,
            photo=photo)
