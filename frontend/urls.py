from django import views
from django.urls import path
from . import views

app_name = 'frontend'
urlpatterns = [
    path('test', views.authorize, name='test'),
    path('login/callback', views.callback, name='callback')
]