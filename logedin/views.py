from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, edit
from .forms import TeamForm
from .models import Team
from users.models import CustomUser
from django import forms
from django.urls import reverse

def currentUserTeams(request):
        teams = {}
        user = CustomUser.objects.get(pk=request.user.pk)
        print(user.pk)
        for i in Team.objects.filter(teamLeader=user):
            teams[i] = i.name
            for j in i.members.filter():
                pass
        print(teams)
        return teams

class HomePageView(TemplateView):
    template_name = 'logedin/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"teams" : currentUserTeams(request)})
class EditTeamView(edit.UpdateView):
    template_name = 'logedin/edit.html'
    model = Team
    fields = ['members']
    def get_success_url(self):
        return reverse("index")
class CreateTeamView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'logedin/createTeam.html'
    def post(self, request):
        form = TeamForm(request.POST)
        if form.is_valid():
            data = {}
            for i in range(len(TeamForm.Meta.fields)):
                data[TeamForm.Meta.fields[i]] = form.cleaned_data[TeamForm.Meta.fields[i]]
            user = CustomUser.objects.get(pk=request.user.pk)
            data['teamLeader'] = user
            form = TeamForm(data)
            print(form)

            form.save()
            return HttpResponse("success")
        return render(request, "logedin/createTeam.html", {"form": form},)
        