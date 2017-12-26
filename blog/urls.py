#!/usr/bin/env python
# coding: utf-8

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('404/', views.page_not_found, name='404'),
    path('', views.view_index, name='index'),
    path('content/', views.view_content, name='content'),
    path('contact/', views.view_contact, name='contact'),
    path('about/', views.view_about, name='about'),
    path('regist/', views.view_regist, name='regist'),
    path('login/', views.view_login, name='login'),
]

handler404 = views.page_not_found
