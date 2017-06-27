from django.conf.urls import url, include
from django.contrib.auth.views import login, logout_then_login
from django.contrib import admin

from .views import app, index, login

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('users.urls')),
    # url(r'^$', app, name='app'),
    url('^auth/login/$', login, name='login'),
    url('^auth/logout/$', logout_then_login, name='logout'),
    url('^$', index, name='index'),
]
