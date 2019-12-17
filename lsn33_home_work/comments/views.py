from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def base(request):
    return HttpResponse(f'You got to the page {str(request.path)} </br> It is "Comments" base page')


def any_right(request, page):
    return HttpResponse(f'You got to the page {str(request.path)} </br> It is "{page}" page ')
