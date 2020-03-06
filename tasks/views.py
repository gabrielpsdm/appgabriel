from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from.forms import *
from rest_framework import status

from .serializer import TaskDataSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)

def deleteTask (request, pk):

    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)

class TaskListView(APIView):
    serializer_class = TaskDataSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Task.objects.all(), many=True)
        return  Response(serializer.data)

    def post(self,request, format=None):
        serializer = self.serializer_class(Task.objects.all(), many=True)
