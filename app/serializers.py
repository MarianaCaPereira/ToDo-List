from app.models import Todo #Class
from rest_framework import serializers #lib

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'done', 'created_at']
