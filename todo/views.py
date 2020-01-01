from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


def destroy(request):
    id = request.GET['todoNum']
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect(reverse('todo.index'))


def index(request):

    todos = Todo.objects.all()
    outs = {'todos': todos}
    return render(request, 'todo/index.html', outs)


def store(request):
    content = request.POST['todoContent']
    todo = Todo(content=content)
    todo.save()
    # return HttpResponse('todo store' + todo.content)
    return HttpResponseRedirect(reverse('todo.index'))
