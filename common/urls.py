from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='detection/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='detection/home.html'), name='logout'),
  path('signup/', views.signup, name='signup'),
]