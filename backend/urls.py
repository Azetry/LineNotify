from django import views
from django.urls import path
from . import views

app_name = 'backend'
urlpatterns = [
    path('test', views.test, name='test'),
]