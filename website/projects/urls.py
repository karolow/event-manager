from django.urls import path
from .views import (
    EventListView,
    ProjectListView,
    FilteredEventTableView,
)

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/filter', FilteredEventTableView.as_view(), name='event_list_filtered'),
]
