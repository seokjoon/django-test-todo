from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='rest'),
    path('create/', views.create, name='rest.create'),
    path('createCat/', views.create_cat, name='rest.createCat'),
    path('createCat/create', views.create_cat_create, name='rest.createCatCreate'),
    path('createCat/destroy', views.destroy_cat, name='rest.destroyCat'),
    path('index', views.index, name='rest.index'),
    path('show/', views.show, name='rest.show'),
]