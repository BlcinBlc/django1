from django.urls import path
from .views import hello, get_user, list_users

urlpatterns = [
    path('hello/', hello),
    path('users/<int:user_id>/', get_user),
    path('users/', list_users),
]