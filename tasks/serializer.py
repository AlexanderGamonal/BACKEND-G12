from rest_framework import serializers
from .models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        # fields = ('id', 'title', 'description', 'done')
        fields = '__all__'