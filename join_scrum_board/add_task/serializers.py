from add_task.models import TaskItem, SubtaskItem, CategoryItem, AssignedContactItem
from main.models import UserAccount
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

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['user', 'username', 'first_name', 'last_name', 'email', 'color', 'phone']
