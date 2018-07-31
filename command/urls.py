#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 20:52
# @Author  : lingxiangxiang
# @File    : urls.py


from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from command import views

urlpatterns = [
    url(r'^$', view=views.index),
]