"""YandexMusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView

from music.views import *
from wall.views import wall, make_repost, add_like

urlpatterns = [
    url('id(?P<user_id>\\d+)', wall, name="wall"),
    url('make_repost/(?P<post_id>\\d+)', make_repost, name="make_repost"),
    url('add_like/(?P<post_id>\\d+)', add_like, name="add_like" )
]