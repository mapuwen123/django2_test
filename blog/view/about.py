#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render


def about(request):
    return render(request, 'blog/about.html')
