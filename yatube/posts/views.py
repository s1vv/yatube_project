from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    return render(request, template, {'title': 'Последние обновления на сайте'})

def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template, {'title': 'Лев Толстой – зеркало русской революции.'})