from rest_framework import serializers
from .models import Todo, Projects

class TodoSerializer(serializers.ModelSerializer):
    title= serializers.CharField(max_length=64)
    task = serializers.CharField(max_length=254)
    priority = serializers.IntegerField()
    deadline = serializers.DateField()

    class Meta:
        model = Todo
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    tasks = TodoSerializer(many=True)

    class Meta:
        model = Projects
        fields = ('name','tasks')