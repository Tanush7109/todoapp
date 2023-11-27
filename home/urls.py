from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tasks/', views.tasks, name="tasks"),
    path('delete/<int:id>', views.delete, name="delete")
]