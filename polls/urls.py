from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('just/', views.just, name='just'),
    path('category/<category_name_slug>', views.show_category, name='show_category')
]
