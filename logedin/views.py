from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, DetailView, ListView, View, edit, detail
from .forms import TeamForm, ApplicationTeamForm
from .models import Team, Membership, Application, Post
from users.models import CustomUser
from django import forms
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin 

# create a mixin that will be used to check if the team leader is the user
class TeamLeaderRequiredMixin(LoginRequiredMixin):
    login_url = 'index'
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user == self.get_object().teamLeader:
            return HttpResponseRedirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)

# create a mixin that will be used to check if the user is a member of the team
class TeamMemberRequiredMixin(LoginRequiredMixin):
    login_url = 'index'
    def dispatch(self, request, *args, **kwargs):
        if not Membership.objects.filter(member=self.request.user, team=self.get_object()).exists():
            return HttpResponseRedirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)
class IsEditorRequiredMixin(LoginRequiredMixin):
    login_url = 'index'
    def dispatch(self, request, *args, **kwargs):
        if not Membership.objects.filter(member=self.request.user, team=self.get_object(), isEditor=True).exists():
            return HttpResponseRedirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)

class TeamsToJoinView(LoginRequiredMixin, ListView):
    login_url = 'signup'
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
        return HttpResponseRedirect(reverse('signup'))
        
    def get(self, request, form, *args, **kwargs):
        
        self.object = self.get_object()
        return render(request, self.template_name, {'team' : self.object, 'form' : form})
    
    def post(self, request, form, *args, **kwargs):
        team = self.get_object()
        form.instance.applicant = request.user
        form.instance.team = team
        form.save()
        return HttpResponseRedirect(reverse('index'))

class AppliedView(LoginRequiredMixin, ListView):
    login_url = 'signup'
    template_name = 'logedin/applied.html'
    context_object_name = 'object'
    def get_queryset(self):
        mySet = {
        "applications": Application.objects.filter(applicant=self.request.user)
        }
        return mySet
# create a post method that will be used to apply to a team
class ListApplicationsView(LoginRequiredMixin, ListView):
    login_url = 'signup'
    template_name = 'logedin/applications.html'
    context_object_name = 'object'
    def get_queryset(self):
        mySet = {
        'applications': Application.objects.filter(team__teamLeader=self.request.user)  
        }
        return mySet
    def post(self, request, *args, **kwargs):
        for i in self.get_queryset()['applications']:
            print(i.applicant.username)
            if i.applicant.username in request.POST:
                Membership.objects.create(member = i.applicant, team = i.team, isLeader = False)
                Application.objects.get(applicant = i.applicant, team = i.team).delete()
                return HttpResponseRedirect(reverse('applications'))
        return HttpResponseRedirect(reverse('index')) 
        
    # create a post method that will be used to apply to a team
class DetailTeamView(TeamLeaderRequiredMixin, DetailView):
    login_url = 'signup'
    model = Team
    template_name = 'logedin/detail.html'

class DetailUserView(LoginRequiredMixin, edit.UpdateView):
    login_url = 'signup'
    model = CustomUser
    template_name = 'logedin/user.html'
    fields = ['username', 'email', 'first_name', 'last_name']
    def get_success_url(self):
        return reverse("user" , kwargs={'pk': self.request.user.pk})
                

class CreatePostView(IsEditorRequiredMixin, CreateView):
    login_url = 'signup'
    model = Post
    template_name = 'logedin/createPost.html'
    fields = ['public', 'content']
    def get_object(self):
        return Team.objects.get(pk=self.kwargs['team'])
    def get_success_url(self):
        return reverse("index")
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.team = self.get_object()
        return super().form_valid(form)
class MyTeamsView(LoginRequiredMixin, ListView):
    login_url = 'home'
    template_name = 'logedin/editors.html'
    context_object_name = 'object'
    def get_queryset(self):
        teams = Team.objects.filter(teamLeader=self.request.user)
        isEditor = teams.count() * [True]
        mySet = {
        'teams': teams,
        'posts': Post.objects.filter(team__teamLeader=self.request.user),
        }
        return mySet
class HomePageView(LoginRequiredMixin, ListView):
    login_url = 'home'
    template_name = 'logedin/index.html'
    fields = []
    context_object_name = 'object'
    def get_queryset(self):
        teams = Team.objects.filter(members__username=self.request.user)

        mySet = {
            'teams': teams,
            'posts': Post.objects.filter(team__members__username=self.request.user),
        }
        return mySet



class EditTeamView(TeamLeaderRequiredMixin, edit.UpdateView):
    login_url = 'signup'
    template_name = 'logedin/edit.html'
    fields = ['name', 'description']
    model = Team
    def get_success_url(self):
        return reverse("index")
class CreateTeamView(LoginRequiredMixin, CreateView):
    login_url = 'signup'
    model = Team
    form_class = TeamForm
    template_name = 'logedin/createTeam.html'
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.teamLeader = self.request.user
            form.instance.save()
            Membership.objects.create(member = form.instance.teamLeader, team = form.instance, isLeader = True, isEditor = True)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form' : form})
    def get_success_url(self):
        return reverse('index')
        