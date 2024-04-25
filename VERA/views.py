from django.shortcuts import render, redirect
from django.http import HttpResponse
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

def home(request):
  #using api
  response = requests.get('https://api.github.com/events')
  data = response.json()
  result = data[0]["id"]
  #result = data[0]["repo"]
  #Response 2
  response2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = response2.json()
  result2 = data2['message']
  return render(request, 'templates/index.html', {'result': result, 'result2': result2})