from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='students_list'),
    path('tasks/', views.task_list, name='tasks_list'),
    path('update/', views.update, name='update'),
    path('delete_info/', views.delete_info, name='delete_info'),
]
