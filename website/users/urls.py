from django.urls import path
from .views import user_update


urlpatterns = [
    path('update/', user_update, name='user_update'),
]
