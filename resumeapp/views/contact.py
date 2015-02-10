# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from resumeapp.models.users import User

def contact_list(request):
    try:
        users = User.objects.all()
    except Exception:
        users = []

    return render(
        request,
        'resume/contact.html',
        {'users': users}
    )
