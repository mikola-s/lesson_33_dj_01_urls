from django.shortcuts import render
from django.http import HttpResponse


# level 01
def base(request):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "{str(request.path).split("/")[1]}" base page')
    return response


def new(request):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "new" in "{str(request.path).split("/")[1]}" page')
    return response


def edit(request):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "edit" in "{str(request.path).split("/")[1]}" page')
    return response


def lock(request):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "lock" in "{str(request.path).split("/")[1]}" page')
    return response

# level 02


def id_base(request, id):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is ID={id} base page in "{str(request.path).split("/")[1]}" page')
    return response


def id_add(request, id):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "{id}.add"  in "{str(request.path).split("/")[1]}" page')
    return response


def id_delete(request, id):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "{id}.base" page in "{str(request.path).split("/")[1]}" page')
    return response


# level 03

def any_right(request, page):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "{page}" in "{str(request.path).split("/")[1]}" page')
    return response
