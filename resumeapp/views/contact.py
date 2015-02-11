# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from resumeapp.models.users import User

def contact_list(request):
    user = []

    try:
        log = request.session['user_log']

        if log:
            user = User.objects.get(login=log)
            return render(request,'resume/home.html',{'user': user})
    except Exception:
        user = []

    return render(
        request,
        'resume/contact.html',
        {'user': user,
        'log': log}
    )
