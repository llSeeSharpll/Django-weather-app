from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  #the path for our index view
    path('place/<str:id>/delete/', views.deleteCity, name='delete_cities'),
]