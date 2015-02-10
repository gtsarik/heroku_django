from django.conf.urls import patterns, include, url
from django.contrib import admin

from resumeapp.views.checkin import CheckInView
from resumeapp.views.private import PrivateView
from .settings import MEDIA_ROOT, DEBUG


urlpatterns = patterns('',
    # Resume urls
    url(r'^$', 'resumeapp.views.resume.resume_list', name='home'),

    # Contact urls
    url(r'^contact/$', 'resumeapp.views.contact.contact_list', name='contact'),

    # Check In urls
    url(r'^checkin/$', CheckInView.as_view(), name='checkin'),
    # url(r'^checkin/$', 'resumeapp.views.checkin.checkin', name='checkin'),

    # LOGIN urls
    url(r'^login/$', 'resumeapp.views.login.login', name='login'),
    url(r'^logout/$', 'resumeapp.views.login.logout', name='logout'),

    # Private url
    url(r'^private/(?P<pk>\d+)/$', PrivateView.as_view(), name='private'),

    # Admin urls
    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))
