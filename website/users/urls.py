from django.urls import path

from .views import account_update, CustomPasswordChangeView

urlpatterns = [
    path('update/', account_update, name='account_update'),
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_password_change'),
]
