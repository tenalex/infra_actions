from django.http import HttpResponse


def index(request):
    return HttpResponse('Привет!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
