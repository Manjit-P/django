from rest_framework import serializers
from todo.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "user",
            "created_on",
            "due",
            "category",
        )