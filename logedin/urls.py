from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('editor/', views.EditorView.as_view(), name='editor'),
    path('applied/', views.AppliedView.as_view(), name='applied'),
    path('application/', views.ListApplicationsView.as_view(), name='applications'),
    path('create/', views.CreateTeamView.as_view(), name='create'),
    path('join/', views.TeamsToJoinView.as_view(), name='join'),
    path('edit/<int:pk>/', views.EditTeamView.as_view(), name='edit'),
    path('detail/<int:pk>/', views.DetailTeamView.as_view(), name='detail'),
    path('user/<int:pk>/', views.DetailUserView.as_view(), name='user'),
    path('apply/<int:pk>/', views.ApplyTeamView.as_view(), name='apply'),
    path('createPost/<int:team>/', views.CreatePostView.as_view(), name='createPost'),
]