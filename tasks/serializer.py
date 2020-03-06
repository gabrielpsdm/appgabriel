from rest_framework import serializers
from .models import Task

class TaskDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        depth = 1
        fields = ['title','complete','created']