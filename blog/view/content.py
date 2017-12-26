#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render, get_object_or_404

from blog.models import Content, Articles


def content(request):
    id = request.GET.get('id')
    article = Articles.objects.get(id=id)
    content = get_object_or_404(Content, id=id)
    return render(request, 'blog/content.html', {'content': content, 'article': article})
