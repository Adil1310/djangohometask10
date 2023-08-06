from django.shortcuts import render
from .models import Student, Task

# Create your views here.

def update(request):
    students = Student.objects.all()
    for student in students:
        student.name = f"{student.name} ({student.id})"
        student.save()

    tasks = Task.objects.all()
    for task in tasks:
        task.task = f"{task.task} ({task.id})"
        task.save()

    return render(request, 'index.html') 

def delete_info(request):
    delete_task = Task.objects.filter(id__mod=2)
    delete_task.delete()

    return render(request, 'taskpage.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'taskpage.html', {'tasks': tasks})
