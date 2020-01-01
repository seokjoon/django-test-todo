from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('todo', views.index, name='todo.index'),
    path('todo/destroy', views.destroy, name='todo.destroy'),
    path('todo/store', views.store, name='todo.store'),
]