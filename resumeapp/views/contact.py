# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from resumeapp.models.users import User

def contact_list(request):
    user = []

    try:
        if request.session['user_log']:
            user = User.objects.get(login=request.session['user_log'])
        else:
            user = User.objects.get(login='gtsarik')
    except Exception:
        user = []
        return render(request,'resume/contact.html',{'user': user})

    return render(
        request,
        'resume/contact.html',
        {'user': user}
    )
