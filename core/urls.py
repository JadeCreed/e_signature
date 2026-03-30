from django.urls import path
from . import views

urlpatterns = [
    path('', views.planting_form, name='planting'),
    path('harvesting/', views.harvesting_form, name='harvesting'),
    path('dashboard/', views.president_dashboard, name='dashboard'),
]