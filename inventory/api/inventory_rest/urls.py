from django.urls import path
from .views import (
    api_list_pellets,
    api_show_pellet,
)

urlpatterns = [
    path("pellets/", api_list_pellets, name="list_pellets"),
    path("pellets/<int:pk>", api_show_pellet, name="show_pellet"),
]
