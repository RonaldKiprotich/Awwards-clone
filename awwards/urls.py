from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views

urlpatterns = [
    
    path('accounts/register/', views.registration, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]