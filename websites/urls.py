from django.urls import path
from . import views

urlpatterns = [
    path('', views.website_list, name='website_list'),
    path('create/', views.website_create, name='website_create'),
]