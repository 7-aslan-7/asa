from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

class TaskListCreateView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskRetrieveUpdateDestroyView(mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
