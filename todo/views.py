from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse('todo index')
    return render(request, 'todo/index.html')