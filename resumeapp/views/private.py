# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib import messages

from ..models.users import User
from ..forms.private import PrivateForm


class PrivateView(UpdateView):
    model = User
    form_class = PrivateForm
    template_name = 'resume/private.html'
    success_message = u'Измения внесены.'
    error_message = u'Возникла ошибка. Попробуйте позже'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return u'%s?status_message=Измения внесены' \
            % (reverse('home'))

    def get_context_data(self, **kwargs):
        context = super(PrivateView, self).get_context_data(**kwargs)
        context['title_page'] = u'Личный кабинет, %s' % (context['user'])
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.success(self.request, 'Изменения отменены')
            return HttpResponseRedirect(
                u'%s?status_message=Изменения отменены' %
                reverse('home'))
        else:
            return super(PrivateView, self).post(request, *args, **kwargs)



