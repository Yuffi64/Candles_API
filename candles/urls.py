from django.urls import path
from . import views


urlspatherns =[
    path('', views.candles_list),
]