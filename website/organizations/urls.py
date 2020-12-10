from django.urls import path
from .views import (
    OrganizationEventTableView,
    AllOrganizationsEventTableView,
    OrganizationProjectTableView,
    AllOrganizationsProjectTableView,
)

urlpatterns = [
    path('events/all/', OrganizationEventTableView.as_view(), name='organization_event_table'),
    path('events/all/follower/', AllOrganizationsEventTableView.as_view(),
         name='all_organizations_event_table'),
    path('projects/all/', OrganizationProjectTableView.as_view(), name='organization_project_table'),
    path('projects/all/follower/', AllOrganizationsProjectTableView.as_view(),
         name='all_organizations_project_table'),
]
