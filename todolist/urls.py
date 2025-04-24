from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name="home"),
    path('add/', views.add_task, name='add-task'),
    path('delete/<int:task_id>', views.delete_task, name="delete-task"),
    path('done/<int:task_id>/', views.toggle_task, name="toggle-task")
]