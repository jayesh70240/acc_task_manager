from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,ProjectViewSet
from .views import ProjectsController
from django.urls import path
router = DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = router.urls + [
    path('projects_list/', ProjectsController.as_view(), name='projects-list'),
]
