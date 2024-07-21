from add_task.models import TaskItem, SubtaskItem, CategoryItem, AssignedContactItem
from rest_framework import serializers


class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = "__all__"

class SubtaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtaskItem
        fields = "__all__"
     
class AssignedContactItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedContactItem
        fields = "__all__"

class CategoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryItem
        fields = "__all__"