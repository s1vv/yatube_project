from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    title = 'Последние обновления на сайте'
    context = {
        'text': text,
        'title': title
    }
    return render(
        request, template, context 
    )


def group_list(request):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    title = 'Лев толстой зеркало русской души'
    context = {
        'text': text,
        'title': title
    }
    return render(
        request, template, context
    )
