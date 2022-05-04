from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='HomePage'),
    path('note/', views.note_single, name='note_single'),
    path('delete/', views.delete, name='DeletePage')

]
