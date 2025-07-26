from rest_framework import generics
from todo.models import Task
from .serializers import TaskSerializer

class TaskApiListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskApiDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'slug'
