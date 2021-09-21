from django.contrib import admin
from django.urls import path
from onlineexam_app import views

urlpatterns = [
    
    path('', views.examonline),
    path('examonline2/', views.examonline2),
    
]
