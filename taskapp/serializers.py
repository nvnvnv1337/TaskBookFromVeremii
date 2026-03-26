from rest_framework import serializers
from .models import Task

#LSP, OCP и DIP
class BaseTaskSerializer(serializers.ModelSerializer):
    class Meta:
        pass

class TaskSerializer(BaseTaskSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['created_at', 'user']

class AdminSerializer(BaseTaskSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = [] 