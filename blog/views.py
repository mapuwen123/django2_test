#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render
from blog.view.content import content
from blog.view.index import index
from blog.view.contact import contact
from blog.view.about import about
from blog.view.regist import regist
from blog.view.login import login
from django.http import HttpResponseNotFound


# Create your views here.
def view_index(request):
    return index(request)


def view_content(request):
    return content(request)


def view_contact(request):
    return contact(request)


def view_about(request):
    return about(request)


def view_regist(request):
    return regist(request)


def view_login(request):
    return login(request)


def page_not_found(request):
    url = request.META.get('HTTP_REFERER', '/')
    print('page_not_found', url)
    return render(request, 'blog/404.html', {'url': url})
