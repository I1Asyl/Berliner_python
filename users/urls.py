from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import customAuthenticationForm
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(authentication_form=customAuthenticationForm), name='login')
]