from django.urls import path
from .views import (
    ProjectListAPIView,
    ProjectRetrieveAPIView,
)


urlpatterns = [
    path('projects/', ProjectListAPIView.as_view()),
    path('projects/<uuid:pk>', ProjectRetrieveAPIView.as_view()),
]
