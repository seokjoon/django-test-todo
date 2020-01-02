from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


def create(request):
    # return HttpResponse('rest create')
    return render(request, 'rest/create.html')


def create_cat(request):
    # return HttpResponse('cat create')
    return render(request, 'rest/createCat.html')


def index(request):
    # return HttpResponse('rest index')
    return render(request, 'rest/index.html')


def show(request):
    # return HttpResponse('rest show')
    return render(request, 'rest/show.html')

