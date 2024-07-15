from django.db import models
from django.conf import settings
from django.db.models.fields import DateField
from datetime import date
#from json_field import JSONField
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Subtask(models.Model):
    subtaskName = models.CharField(max_length=50)
    status = models.CharField(max_length=6)

class Assigned_to(models.Model):
    pass

class Task(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = DateField(default=date.today)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    due_date = models.DateField()
    priority = models.CharField(max_length=50)
    subtasks = Subtask
    assigned_to = ArrayField()
    status = models.CharField(max_length=50)
    

