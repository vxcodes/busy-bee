from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('combs/', views.combs_index, name='index'),
    path('combs/<int:comb_id>/', views.combs_detail, name='detail'),
]