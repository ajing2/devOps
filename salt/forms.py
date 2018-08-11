#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 20:41
# @Author  : lingxiangxiang
# @File    : forms.py
from django import forms


class SystemInit(forms.Form):
    iptext = forms.CharField(max_length=1000)
    checkbox = forms.MultipleChoiceField()
    # forms.MultipleChoiceField