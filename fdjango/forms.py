from django import forms
from fdjango.models import Project ,Visit

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields= "__all__"

class VisitForm(forms.ModelForm):
    class Meta:
        model=Visit
        fields= "__all__"