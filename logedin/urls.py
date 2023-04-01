from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('create/', views.CreateTeamView.as_view(), name='create')
]