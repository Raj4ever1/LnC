from django.urls import path

from api.authentication import views

urlpatterns = [
    path('signup/html', views.createUserForm),
    path('signup/', views.createUser),
    path('login/', views.loginUser),
    path('logout/', views.logoutUser),
]
