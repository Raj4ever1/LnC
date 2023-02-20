from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.get_teams),
]
