from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('airports/', views.airport_list),
    path('airports/<str:ident>/', views.airport_ident)
]