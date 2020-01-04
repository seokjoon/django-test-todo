from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


def create(request):
    # return HttpResponse('rest create')
    return render(request, 'rest/create.html')


def create_cat(request):
    # return HttpResponse('cat create')
    cats = RestCat.objects.all()
    content = {'categories': cats}
    return render(request, 'rest/createCat.html', content)


def create_cat_create(request):
    # return HttpResponse('todo')
    title = request.POST['categoryName']
    cat = RestCat(title = title)
    cat.save()
    return HttpResponseRedirect(reverse('rest.index'))


def destroy_cat(request):
    id = request.POST['categoryId']
    cat = RestCat.objects.get(id=id)
    cat.delete()
    return HttpResponseRedirect(reverse('rest.createCat'))


def index(request):
    # return HttpResponse('rest index')
    cats = RestCat.objects.all()
    content = { 'categories': cats }
    return render(request, 'rest/index.html', content)


def show(request):
    # return HttpResponse('rest show')
    return render(request, 'rest/show.html')

