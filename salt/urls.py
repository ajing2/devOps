#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 20:52
# @Author  : lingxiangxiang
# @File    : urls.py

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from salt import views
from django.contrib.auth.models import User

urlpatterns = [
    url(r'^$', view=views.index),
    url(r'installapp/$', view=views.installApp),
    url(r'applist/$', view=views.applist),
    url(r'init/$', view=views.init),
]