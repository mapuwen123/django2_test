#!/usr/bin/env python
# coding: utf-8

from django.contrib import admin
from .models import Articles, Content, Contact, User
from django.core.cache import cache


# Register your models here.
class ContentInline(admin.TabularInline):
    model = Content


class ArticlesAdmin(admin.ModelAdmin):
    # 列表展示字段
    list_display = (
        'id',
        'title',
        'date',
    )
    inlines = [
        ContentInline,
    ]
    # 每页展示条数
    list_per_page = 25
    # 排序
    ordering = (
        '-date',
    )

    search_fields = ('title',)  # 搜索字段

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        article_list = Articles.objects.order_by('-date')
        cache.set('article_list', article_list)


admin.site.register(Articles, ArticlesAdmin)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
    )
    list_per_page = 25
    ordering = (
        '-id',
    )

    search_fields = ('name',)  # 搜索字段


admin.site.register(User)
