# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from resumeapp.models.users import User

def contact_list(request):
    user = []

    auth = request.session['user_auth']
    log = request.session['user_log']

    try:
        if request.session['user_auth']:
            user = User.objects.get(login=request.session['user_log'])
            return render(request,'resume/home.html',{'user': user})
    except Exception:
        user = []

    return render(
        request,
        'resume/contact.html',
        {'user': user,
        'log': log,
        'auth': auth}
    )
