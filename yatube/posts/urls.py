from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='home'),
    path('index.html', views.index, name='home'),
    path('group_list.html', views.group_list, name='group_list'),
]
