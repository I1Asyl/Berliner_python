from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import TeamForm
from users.models import CustomUser
class HomePageView(TemplateView):
    template_name = 'index.html'


def get_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            data = {}
            for i in range(len(TeamForm.Meta.fields)):
                data[TeamForm.Meta.fields[i]] = form.cleaned_data[TeamForm.Meta.fields[i]]
            user = CustomUser.objects.get(pk=request.user.pk)
            data['teamLeader'] = user
            form = TeamForm(data)
            form.save()
    else:
        form = TeamForm()
    return render(request, 'createTeam.html', {'form': form})
        