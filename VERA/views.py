from django.shortcuts import render, redirect #django shortcuts
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("Hello Vera! Welcome to Django Website")

from .models import Task
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'VERA/task_list.html', {'tasks': tasks})
def add_task(request):
    if request.method =='POST':
        title= request.POST['title']
        Task.object.create(title=title)
        return redirect(task_list)
    
def delete_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('task_list') #just refreshes the browser