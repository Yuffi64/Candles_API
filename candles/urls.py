from django.urls import path
from . import views


urlpatterns =[
    path('', views.fragrant_list),
    path('<int:pk>/', views.fragrant_detail)
]