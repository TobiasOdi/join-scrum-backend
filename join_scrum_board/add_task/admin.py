from django.contrib import admin
from add_task.models import TaskItem, SubtaskItem

# Register your models here.
admin.site.register(TaskItem)
admin.site.register(SubtaskItem)