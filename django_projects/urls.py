"""django_projects URL Configuration

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
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from vooks.views import *
from vooks.forms import LoginForm

urlpatterns = [
    url(r'^$', index, name='index'),
    path('mypage/', mypage, name='mypage'),

    path('regist/', regist, name='regist'),
    path('regist_save/', regist_save, name='regist_save'),
    
    url(r'^login/$', login, {
        'template_name': 'login.html', 
        'authentication_form': LoginForm
        }, name='login'),
    
    url(r'^logout/$', logout, {
        'template_name': 'index.html'
        }, name='logout'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]