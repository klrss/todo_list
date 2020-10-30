from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import TodoForm, ProjectForm
from .models import Todo, Projects
from django.core import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer, ProjectsSerializer

content = []

# Create your views here.
@api_view(['GET'])
def indexView(request):
    todo_urls = {
        'List': '/task-list',
        'Create':'/task-create',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(todo_urls)

@api_view(['GET'])
def todolist(request):
    tasks = Todo.objects.all()
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)

# index with a form for adding task and viewing the list of task
def index(request):
    names = Projects.objects.all()
    tasks = Todo.objects.all()
    if request.method == 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
                        
    return render(request, "index.html",{"form":TodoForm(),"names":names,"tasks":tasks})
    
# add title of project
def add(request):
    names = Projects.objects.all()
    if request.method == 'POST':
        form_names = ProjectForm(request.POST)
        if form_names.is_valid ():
            form_names.save()
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request,"add.html", {"form_names":form_names})

    return render(request,"add.html", {"form_names": ProjectForm(),"names":names})

# update task
def updateTask(request, pk):
    task = Todo.objects.get(id=pk)
    form = TodoForm(instance=task)
    if request.method =='POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse("todo:index"))
    return render(request,"update_task.html",{"form":form})

# update title, a name of project
def updateProject(request, pk):
    name = Projects.objects.get(id=pk)
    form_name = ProjectForm(instance=name)
    if request.method =='POST':
        form_name = ProjectForm(request.POST, instance=name)
        if form_name.is_valid():
            form_name.save()
            return  HttpResponseRedirect(reverse("todo:index"))
    return render(request,"update_project.html",{"form_name":form_name})

#remove task
def removeTask(request, pk):
    Todo.objects.filter(id=pk).delete()
    if request.method=="POST":
        return HttpResponseRedirect(reverse("todo:index"))
    return render(request,"remove_task.html",{})
# remove a name of project
def removeProject(request, pk):
    Projects.objects.filter(id=pk).delete()
    if request.method=="POST":
        return HttpResponseRedirect(reverse("todo:index"))
    return render(request,"remove_project.html",{})
   
