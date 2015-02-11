# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.contrib import messages

from settings import ADMIN_EMAIL
from ..models.users import User
from ..forms.checkin import CheckInForm


class CheckInView(CreateView):
    model = User
    form_class = CheckInForm
    template_name = 'login/checkin.html'
    success_message = u'Регистрация прошла успешно.'
    error_message = u'Во время регистрации возникла ошибка. \
                    Попробуйте позже'

    def get_success_url(self):
        try:
            email = self.request.POST['email']
            login = self.request.POST['login']
            password = self.request.POST['password']
            head = u'%s, здравствуйте!' % login
            body = u'''Поздравляем. Вы успешно зарегистрировались.
                    логин: %s
                    пароль: %s'''  % (login, password)
            send_mail(head, body, ADMIN_EMAIL, [email])
        except Exception as e:
            self.error_message += u' %s' % e
            messages.error(self.request, self.error_message, extra_tags='warning')

            return u'%s?status_message=Во время регистрации возникла ошибка' \
            % (reverse('checkin'))
        else:
            self.request.session['user_log'] = u''
            log_name = unicode.encode(self.request.POST.get(u'login', ''), 'utf8')
            success_message = 'Пользователь %s успешно зарегистрирован.' % (
                log_name)
            messages.success(self.request, success_message)
        
        return u'%s?status_message=Регистрация прошла успешно' \
            % (reverse('login'))

    def get_context_data(self, **kwargs):
        context = super(CheckInView, self).get_context_data(**kwargs)
        context['title_page'] = u'Добавить пользователя'

        return context
