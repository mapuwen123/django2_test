#!/usr/bin/env python
# coding: utf-8
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from blog.models import User


def regist(request):
    if request.POST:
        name = request.POST['name']
        password = make_password(request.POST['password'])
        print('PASSWORD:', password)
        User.objects.create(
            name=name,
            password=password,
        )
        return render(request, 'blog/login.html')
    else:
        return render(request, 'blog/regist.html')
