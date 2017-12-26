#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render

from blog.models import Contact


def contact(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact.objects.create(
            name=name,
            email=email,
            message=message,
        )
        return render(request, 'blog/contact.html', {'result': name})
    else:
        return render(request, 'blog/contact.html')
