from django.conf.urls import url
from sitechan.views import *


urlpatterns = [
    url(r'^$', show_messages),
    url(r'^send/$', send),
    url(r'^reply/(?P<message_id>\d+)$', reply),
    url(r'^response/(?P<message_id>\d+)$', response),
]