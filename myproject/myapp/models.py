from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Task(models.Model):
    task = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task