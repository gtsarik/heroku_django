# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib import messages
import hashlib

from settings import SALT_KEY
from ..models.users import User
from ..forms.login import UserLoginForm


def login(request):
    if request.POST:
        form = UserLoginForm(request.POST)
        login = request.POST['login']
        password = request.POST['password']
        request.session['user_auth'] = u''
        request.session['user_log'] = u''
        request.session['user_img'] = u''
        request.session['user_id'] = u''

        try:
            password += SALT_KEY
            hash_password = hashlib.sha224(password).hexdigest()
            user = User.objects.get(login=login, password=hash_password)
            user_auth = user.first_name + u' ' + user.last_name[0].upper() + '.'

            if user.photo:
                request.session["user_img"] = str(user.photo)

            request.session['user_auth'] = user_auth
            request.session['user_log'] = user.login
            request.session['user_id'] = user.id

            return HttpResponseRedirect(reverse('home'))
        except Exception:
            messages.warning(request, u'Пользовтель не найден.')
    else:
        form = UserLoginForm()
    
    return render(request, 'login/login.html', {'form': form, 'title_page': u'Авторизация'})


def logout(request):
    request.session['user_auth'] = u''
    request.session['user_log'] = u''
    request.session['user_img'] = u''
    request.session['user_id'] = u''
    
    return HttpResponseRedirect(reverse('home'))
