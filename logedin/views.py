from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, DetailView, ListView, View, edit, detail
from .forms import TeamForm, ApplicationTeamForm
from .models import Team, Membership, Application
from users.models import CustomUser
from django import forms
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin 

# create a mixin that will be used to check if the team leader is the user
class TeamLeaderRequiredMixin(LoginRequiredMixin):
    login_url = 'home'
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user == self.get_object().teamLeader:
            return HttpResponseRedirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)

# create a mixin that will be used to check if the user is a member of the team
class TeamMemberRequiredMixin(LoginRequiredMixin):
    login_url = 'home'
    def dispatch(self, request, *args, **kwargs):
        if not Membership.objects.filter(member=self.request.user, team=self.get_object()).exists():
            return HttpResponseRedirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)


class TeamsToJoinView(LoginRequiredMixin, ListView):
    login_url = 'home'
    template_name = 'logedin/join.html'
    fields = []
    def get_queryset(self):
        return Team.objects.exclude(members=self.request.user).exclude(applicants=self.request.user)
    # create a post method that will be used to apply to a team

class ApplyTeamView(detail.SingleObjectMixin, View):
    template_name = 'logedin/apply.html'
    model = Team
    form_class = ApplicationTeamForm
    # create a post method that will be used to apply to a team
    def dispatch(self, request, *args, **kwargs):
        if(self.request.user.is_authenticated):
            if request.method == 'POST':
                form = self.form_class(request.POST)
                return self.post(request, form, *args, **kwargs)
            else:
                form = self.form_class()
                return self.get(request, form, *args, **kwargs)
        return HttpResponseRedirect(reverse('home'))
        
    def get(self, request, form, *args, **kwargs):
        
        self.object = self.get_object()
        return render(request, self.template_name, {'team' : self.object, 'form' : form})
    
    def post(self, request, form, *args, **kwargs):
        team = self.get_object()
        form.instance.applicant = request.user
        form.instance.team = team
        form.save()
        return HttpResponseRedirect(reverse('index'))

class ApplicationsView(LoginRequiredMixin, ListView):
    login_url = 'home'
    template_name = 'logedin/applications.html'
    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)
# create a post method that will be used to apply to a team
class AcceptApplicationView(TeamLeaderRequiredMixin, DetailView):
    login_url = 'home'
    template_name = 'logedin/accept.html'
    model = Team
    fields = []
    # create a post method that will be used to apply to a team
class DetailTeamView(LoginRequiredMixin, DetailView):
    login_url = 'home'
    model = Team
    template_name = 'logedin/detail.html'

class HomePageView(LoginRequiredMixin, ListView):
    login_url = 'home'
    template_name = 'logedin/index.html'
    def get_queryset(self):
        return Team.objects.filter(teamLeader=self.request.user)
class EditTeamView(TeamLeaderRequiredMixin, edit.UpdateView):
    login_url = 'home'
    template_name = 'logedin/edit.html'
    fields = ['name', 'description']
    model = Team
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
            Membership.objects.create(member = form.instance.teamLeader, team = form.instance, isLeader = True)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form' : form})
    def get_success_url(self):
        return reverse('index')
        