# -*- coding: utf-8 -*-

import os

from .settings import PORTAL_URL
from .urls import urlpatterns
from resumeapp.models.users import User


def absoluteResumeUrl(request):
    '''Returns absolute site root '''

    separ = os.sep
    domen_url_list = request.build_absolute_uri().split(separ)
    domen_url = domen_url_list[0] + separ + separ + domen_url_list[2]

    return {'DOMEN_URL': domen_url}


def activePage(request):
    on_homepage = False
    on_contact = False
    on_private = False
    page_path = request.get_full_path()

    if '/' in page_path \
        and '/contact' not in page_path\
        and '/private' not in page_path\
        and '/login' not in page_path\
        and '/checkin' not in page_path:
        on_homepage = True
    if '/contact' in page_path:
        on_contact = True
    if '/private' in page_path:
        on_private = True

    return {'HOMEPAGE': on_homepage,
        'CONTACT': on_contact,
        'PRIVATE': on_private}


def pathToPhoto(request):
    user_photo = ''

    try:
        login = request.session["user_log"]
        if login:
            user = User.objects.get(login=login)
            user_photo = user.photo
    except Exception:
        user_photo = ''

    return {'PHOTO_PATH': user_photo}
