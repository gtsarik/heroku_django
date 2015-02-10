# -*- coding: utf-8 -*-

from django import forms
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserLoginForm(forms.Form):

    login = forms.CharField(
        label=u'Имя пользователя',
        required=True
    )

    password = forms.CharField(
        label=u'Пароль',
        required=True,
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('login')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-3 control-label'
        self.helper.field_class = 'col-sm-9'

        # form buttons
        self.helper.add_input(Submit('send_button', u'Войти', css_class="btn btn-primary"),)
