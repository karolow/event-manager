from rest_framework.routers import SimpleRouter

from .views import (
    EventViewSet,
    ProjectViewSet,
    # UserViewSet,
)


router = SimpleRouter()
router.register('events', EventViewSet, basename='events')
router.register('projects', ProjectViewSet, basename='projects')

urlpatterns = router.urls
