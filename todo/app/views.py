from django.shortcuts import render
from .models import *
from django.http import HttpResponse
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