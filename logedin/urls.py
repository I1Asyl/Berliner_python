from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('create/', views.CreateTeamView.as_view(), name='create'),
    path('join/', views.JoinTeamView.as_view(), name='join'),
    path('edit/<int:pk>/', views.EditTeamView.as_view(), name='edit'),
    path('detail/<int:pk>/', views.DetailTeamView.as_view(), name='detail'),
]