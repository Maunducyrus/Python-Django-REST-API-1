from django.urls import path

from .views import get_user

urlpatterns = [
    path('users/', get_user, name='user'),
]