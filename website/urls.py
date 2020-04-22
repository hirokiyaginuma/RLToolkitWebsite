from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('installing/', views.installing, name='installing'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('contact/', views.contact, name='contact'),
]