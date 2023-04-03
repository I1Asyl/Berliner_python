from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, edit, DetailView, ListView
from .forms import TeamForm
from .models import Team, Membership
from users.models import CustomUser
from django import forms
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin 

class JoinTeamView(LoginRequiredMixin, ListView):
    login_url = 'home'
    template_name = 'logedin/index.html'
    def get_queryset(self):
        return Membership.objects.exclude(member=self.request.user)    

class DetailTeamView(LoginRequiredMixin, DetailView):
    login_url = 'home'
    model = Team
    template_name = 'logedin/detail.html'

class HomePageView(LoginRequiredMixin, ListView):
    login_url = 'home'
    template_name = 'logedin/index.html'
    def get_queryset(self):
        return Team.objects.filter(teamLeader=self.request.user)
class EditTeamView(LoginRequiredMixin, edit.UpdateView):
    login_url = 'home'
    template_name = 'logedin/edit.html'
    model = Team
    fields = ['members']
    def get_success_url(self):
        return reverse("index")
class CreateTeamView(LoginRequiredMixin, CreateView):
    login_url = 'home'
    model = Team
    form_class = TeamForm
    template_name = 'logedin/createTeam.html'
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.teamLeader = self.request.user
            form.instance.save()
            form.instance.members.add(self.request.user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form' : form})
    def get_success_url(self):
        return reverse('index')
        