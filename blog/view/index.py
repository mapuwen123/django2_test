#!/usr/bin/env python
# coding: utf-8

from django.core.cache import cache
from django.shortcuts import render

from blog.models import Articles
from django.contrib.sessions.models import Session


def index(request):
    request.session['username'] = 'mapuwen'
    request.session['password'] = '274226ma'
    user_dict = request.session.get('user_dict', default=None)
    s = Session.objects.get(pk=request.session.session_key)
    print(request.session.session_key)
    print(s.get_decoded())
    # if not user_dict is None:
    # print('INDEX_1:', user_dict)
    # request.session.delete(request.session.session_key)
    article_list = cache.get('article_list')
    print(article_list)
    if article_list is None:
        article_list = Articles.objects.order_by('-date')
        cache.set('article_list', article_list, timeout=60 * 20)
    return render(request, 'blog/index.html', {'article_list': article_list})
    # else:
    #     print('INDEX_2:', user_dict)
    #     return HttpResponseRedirect(reverse('blog:login'))

    # # 每页显示条数
    # limit = 3
    # # 数据库查询
    # article_list = Articles.objects.all()
    # # 定义分页
    # paginator = Paginator(article_list, limit)
    # # 从GET请求获取页码
    # page = request.GET.get('page')
    # try:
    #     article_list = paginator.page(page)
    # except PageNotAnInteger:  # 页码过小
    #     article_list = paginator.page(1)
    # except EmptyPage:  # 页码过大
    #     article_list = paginator.page(paginator.num_pages)
    # return render(request, 'blog/index.html', {'article_list': article_list})
