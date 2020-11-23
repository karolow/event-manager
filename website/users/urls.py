from django.urls import path

from .views import (
    account_update,
    CustomPasswordChangeView,
    APIManagementView,
)

urlpatterns = [
    path('update/', account_update, name='account_update'),
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_password_change'),
    path('api/manage/', APIManagementView.as_view(), name='account_api'),
]
