from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello my frinds')


def second_page(request):
    return HttpResponse('А это вторая страница!')
