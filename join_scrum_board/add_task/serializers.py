from add_task.models import TaskItem, SubtaskItem
from rest_framework import serializers


class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = "__all__"

class SubtaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtaskItem
        fields = "__all__"