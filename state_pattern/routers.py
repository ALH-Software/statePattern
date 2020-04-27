from rest_framework import routers
from task_manager.viewsets import TaskViewSet

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, basename='task')
