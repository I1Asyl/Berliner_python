from django import forms
from . models import Team, Application

#form for creating a team
class TeamForm(forms.ModelForm):
  #Meta class is used to define the model and fields that are used in the form
  class Meta:

    model = Team
    fields = ['name', 'description']

class ApplicationTeamForm(forms.ModelForm):
  #Meta class is used to define the model and fields that are used in the form
  class Meta:

    model = Application
    fields = ['comment'] 