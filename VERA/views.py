from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import Task
import requests

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'VERA/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('task_list')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('task_list')

def hello(request):
    return HttpResponse("Hello Vera! Welcome to Django Website")
def chuck_norris_joke(request):
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

    