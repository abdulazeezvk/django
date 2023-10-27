from django.contrib import admin
from django.urls import path
from .import views

app_name='myapp'

urlpatterns = [
    
    path('',views.index, name ='course'),
    path('courses/<int:pk>/', views.detail, name='detail'),
]