from django.conf import settings
from django.conf.urls import patterns, include, url

from {{ project_name }}.urls import *

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True,
    }),
)