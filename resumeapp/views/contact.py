# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from resumeapp.models.users import User

def contact_list(request):
    user = []
    log = u''

    try:
        log = request.session['user_log']

        if log:
            user = User.objects.get(login=request.session['user_log'])
    except Exception:
        user = []
        return render(request,'resume/home.html',{'user': user})

    return render(
        request,
        'resume/contact.html',
        {'user': user,
        'log': log}
    )
