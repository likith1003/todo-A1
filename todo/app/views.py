from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def home(request):
    alltodos = Todo.objects.all()
    d = {'alltodos': alltodos}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        if title and desc:
            todo = Todo(title=title, desc=desc)
            todo.save()
    return render(request, 'home.html', d)


def update(request,pk):
    TO = Todo.objects.get(pk=pk)
    d = {'TO': TO}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        TO.title=title
        TO.desc=desc
        TO.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'update.html', d)

def delete(request, pk):
    TO = Todo.objects.get(pk=pk)
    TO.delete()
    return HttpResponseRedirect(reverse('home'))