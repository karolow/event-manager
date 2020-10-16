from django.urls import path
from .views import (
    ProjectListView,
    EventListView,
)

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('events/', EventListView.as_view(), name='event_list'),
]
