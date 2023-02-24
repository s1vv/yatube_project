from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница приложения post')


def group_posts(request):
    return HttpResponse('Страницы сообщества')


def group_posts_name(request, pk):
    return HttpResponse(f'Страницы сообщества {pk}')
