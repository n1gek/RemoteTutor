from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from datetime import timezone

# Create your models here.
class Student(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class Message(models.Model):
    value = models.CharField(max_length=100000)
    date = models.DateTimeField(default=timezone, blank=True)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)


