from django.db import models
from django.conf import settings
from django.db.models.fields import DateField
from datetime import date
#from json_field import JSONField
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


# Create your models here.
class TaskItem(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = DateField(default=date.today)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=25)
    due_date = models.DateField()
    priorityValue = models.CharField(max_length=10)
    #assigned_to = ArrayField()
    statusCategory = models.CharField(max_length=25, default='toDo')
    
    def __str__(self):
        return f"({self.id}) {self.title}"

class SubtaskItem(models.Model):
    parent_task_id = models.ForeignKey(TaskItem, on_delete=models.CASCADE, default=None)
    #created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    subtaskName = models.CharField(max_length=50)
    status = models.CharField(max_length=6)
    
    def __str__(self):
        return f"({self.id}) {self.subtaskName}"

class AssignedContactItem(models.Model):
    parent_task_id = models.ForeignKey(TaskItem, on_delete=models.CASCADE, default=None)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    contactColor = models.CharField(max_length=25)   

class CategoryItem(models.Model):
    categoryName = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    categoryType = models.CharField(max_length=25)
    
    def __str__(self):
        return f"({self.id}) {self.categoryName}"
    
""" class ContactItem(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=50)
    contactColor = models.CharField(max_length=25)   
    
    def __str__(self):
        return f"({self.id}) {self.email}" """
