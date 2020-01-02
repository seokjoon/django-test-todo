from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index),
    path('', views.index, name='todo.index'),
    path('/destroy', views.destroy, name='todo.destroy'),
    path('/store', views.store, name='todo.store'),
]