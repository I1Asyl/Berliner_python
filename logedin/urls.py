from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',  login_required(views.HomePageView.as_view(), login_url='/welcome[]'), name='index'),
    path('create/', views.CreateTeamView.as_view(), name='create'),
    path('edit/<int:pk>/', views.EditTeamView.as_view(), name='edit')
]