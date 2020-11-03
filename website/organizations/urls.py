from django.urls import path
from .views import (
    MajorTableView,
)

urlpatterns = [
    path('events/', MajorTableView.as_view(), name='major_event_table'),
]
