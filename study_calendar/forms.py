from django import forms
from django.forms.utils import ErrorList

from .models import TimeTable


class NewTimeTableForm(forms.ModelForm):
    #name = forms.CharField(max_length=255)
    #description = forms.CharField(max_length=
    #study_group = forms.ChoiceField(choices=())


    class Meta:
        model = TimeTable
        fields = ('name', 'description')


class EditTimeTableForm(forms.ModelForm):

    class Meta:
        model = TimeTable
        fields = ('name', 'description', 'owner')
