from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from .models import Task, Project
from .serializers import TaskSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        project_id = instance.id
        self.perform_destroy(instance)
        return Response(
            {"message": f"Project {project_id} deleted successfully."},
            status=status.HTTP_200_OK
        )
    

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'project', 'deadline']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        task_id = instance.id
        self.perform_destroy(instance)
        return Response(
            {"message": f"Task {task_id} deleted successfully."},
            status=status.HTTP_200_OK
        )
    


class ProjectsController(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        project_id = request.query_params.get('id')
        project = get_object_or_404(Project, id=project_id)
        serializer = ProjectSerializer(project, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        project_id = request.query_params.get('id')
        project = get_object_or_404(Project, id=project_id)
        project.delete()
        return Response({"message": f"Project {project_id} deleted successfully."}, status=status.HTTP_200_OK)