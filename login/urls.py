from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/success', views.register_success, name='register_success'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_view.LogoutView.as_view(), {'next_page':'/',}, name='logout'),
]