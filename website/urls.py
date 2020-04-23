from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('get-started/', views.get_started, name='get_started'),
    path('installing/', views.installing, name='installing'),
    path('usage/', views.usage, name='usage'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('contact/', views.contact, name='contact'),
]