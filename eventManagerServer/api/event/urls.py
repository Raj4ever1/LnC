from django.urls import path

from api.event import views

urlpatterns = [
    path('events/', views.events),
    path('events/<int:event_id>', views.event_details)
]
