from django.urls import path

from . import views

app_name = 'detection'

urlpatterns = [
  path('', views.index),
  path('dataset/', views.dataset),
]