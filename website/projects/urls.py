from django.urls import path
from .views import (
    ProjectTableView,
    ProjectCreateView,
    ProjectDetailView,
    ProjectUpdateView,
    duplicate_project,
    ProjectDeleteView,
    EventTableView,
    EventCreateView,
    EventDetailView,
    EventUpdateView,
    duplicate_event,
    EventDeleteView,
    LocationCreateView,
    TextEventInfoView,
)

urlpatterns = [
    path('projects/', ProjectTableView.as_view(), name='project_table'),
    path('projects/new/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<uuid:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<uuid:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<uuid:pk>/duplicate/', duplicate_project, name='project_duplicate'),
    path('projects/<uuid:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('events/', EventTableView.as_view(), name='event_table'),
    path('events/new/', EventCreateView.as_view(), name='event_create'),
    path('events/<uuid:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/<uuid:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('events/<uuid:pk>/duplicate/', duplicate_event, name='event_duplicate'),
    path('events/<uuid:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('events/<uuid:pk>/txt/', TextEventInfoView.as_view(), name='event_txt_info'),
    path('locations/new/', LocationCreateView.as_view(), name='location_create'),

]
