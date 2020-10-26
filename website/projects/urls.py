from django.urls import path
from .views import (
    ProjectListView,
    ProjectCreateView,
    EventTableView,
    EventCreateView,
    EventDetailView,
    EventUpdateView,
    duplicate_event,
    EventDeleteView,
)

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/new/', ProjectCreateView.as_view(), name='project_create'),
    path('events/', EventTableView.as_view(), name='event_table'),
    path('events/new/', EventCreateView.as_view(), name='event_create'),
    path('events/<uuid:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/<uuid:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('events/<uuid:pk>/duplicate/', duplicate_event, name='event_duplicate'),
    path('events/<uuid:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
]
