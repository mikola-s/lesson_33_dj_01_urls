from django.shortcuts import render
from django.http import HttpResponse


def base(request):
    return HttpResponse(f'You got to the page {str(request.path)} </br> It is base IDs page ')


def id_base(request, id):
    return HttpResponse(f'You got to the page {str(request.path)} </br> It is ID={id} base page ')


def id_add(request, id):
    return HttpResponse(f'You got to the page {str(request.path)} </br> It is ID={id} "add" page ')


def id_delete(request, id):
    return HttpResponse(f'You got to the page {str(request.path)} </br> It is ID={id} "delete" page ')
