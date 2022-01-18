from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('sobre/', views.sobre, name='index'),
]
