from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('just/', views.just, name='just')
]