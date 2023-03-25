# user_auth/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'user_auth'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('', views.user_login, name='login_old'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('show_user/', views.show_user, name='show_user'),
    path('register/', views.register, name='register'),
    path('registration_success/', views.registration_success, name='registration_success'),
    
]
