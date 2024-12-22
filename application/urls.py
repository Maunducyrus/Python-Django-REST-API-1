from django.urls import path

from .views import get_users, create_user

urlpatterns = [
    path('users/', get_users, name='get_users'),
    # path to the end point
    path('users/create/', create_user, name='create_user'),
    # url for all users
    path('users/<int:pk>', create_user, name='create_user'),

]