from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from .forms import TeamForm
from .models import Team
from users.models import CustomUser

class HomePageView(TemplateView):
    template_name = 'logedin/index.html'
    def get(self, request, *args, **kwargs):
        dict = {}
        user = CustomUser.objects.get(pk=request.user.pk)
        for i in Team.objects.filter(teamLeader=user):
            dict[i.name] = i.pk
        return render(request, self.template_name, {"teams" : dict})

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
            form.save()
            return HttpResponse("success")
        return render(request, "logedin/createTeam.html", {"form": form},)
        