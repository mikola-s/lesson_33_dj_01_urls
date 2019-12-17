from django.shortcuts import render
from django.http import HttpResponse


def base(request):
    return HttpResponse(f'You got to the page {str(request.path)} </br> It is "News" base page ')


def new(request):
    pass


def edit(request):
    pass


def lock(request):
    pass
