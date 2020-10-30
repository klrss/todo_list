from django.urls import path
from . import views


app_name = "todo"

urlpatterns = [
    path("", views.index, name = "index"),
    path("add", views.add, name = "add"),
    path("update_task/<str:pk>/", views.updateTask, name="update_task"),
    path("update_project/<str:pk>/", views.updateProject, name="update_project"),
    path("remove_task/<str:pk>/", views.removeTask, name ="remove_task"),
    path("remove_project/<str:pk>/", views.removeProject, name ="remove_project"),
    path('task',views.indexView, name="task"), 
    path('task-list', views.todolist, name="todo-list"), 
    

]