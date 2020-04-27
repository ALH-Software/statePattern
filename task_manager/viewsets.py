from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(methods=['get', 'post'], detail=True)
    def edit_title(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)

        if(task.state == 0):
            if request.method == 'GET':
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            else:
                print(request.data)
                task.title = request.data['title']
                task.save()
                serializer = TaskSerializer(task)
                return Response(serializer.data)

    @action(methods=['get', 'post'], detail=True)
    def edit_description(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)

        if(task.state == 0):
            if request.method == 'GET':
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            else:
                print(request.data)
                task.description = request.data['description']
                task.save()
                serializer = TaskSerializer(task)
                return Response(serializer.data)

    @action(methods=['get', 'post'], detail=True)
    def change_state(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        
        if request.method == 'POST':
            if(task.state == 0):
                task.state = 1
            elif(task.state == 1):
                task.state = 2

        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    @action(methods=['get', 'post'], detail=True)
    def link_tasks(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        
        if request.method == 'POST':
            if(task.next == -1):
                task.next = request.data['next']

        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)