from django.urls import path
from . import views
from .views import chuck_norris_joke

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    #apis    
    path('joke/', chuck_norris_joke, name='chuck_norris_joke'),

]