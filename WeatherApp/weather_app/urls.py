from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('<str:city_name>/', views.deleteCity, name="deleteCity")
]
