#!/usr/bin/env python
# coding: utf-8
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from blog.models import User


def login(request):
    if request.POST:
        # token_id = request.POST['token_id']
        name = request.POST['name']
        password = request.POST['password']
        user = User.objects.get(name=name)
        if check_password(password, user.password):
            user_dict = {
                'name': name,
                'password': password,
            }
            request.session['user_dict'] = user_dict
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            return render(request, 'blog/login.html')
    else:
        return render(request, 'blog/login.html')
