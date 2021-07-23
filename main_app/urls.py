from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('combs/', views.combs_index, name='index'),
    path('combs/<int:comb_id>/', views.combs_detail, name='detail'),
    path('combs/create/', views.CombCreate.as_view(), name="combs_create"),
    # path('combs/<int:comb_id>/create-goal/', views.add_goal, name="goals_add"),
    path('combs/create-goal/', views.GoalCreate.as_view(), name="goals_create"),
    path('combs/<int:pk>/update/', views.CombUpdate.as_view(), name='combs_update'),
    path('combs/<int:pk>/delete/', views.CombDelete.as_view(), name='combs_delete'),
]