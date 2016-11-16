from django import forms
from django.forms.utils import ErrorList

from .models import TimeTable
from comments.models import Comment


class NewTimeTableForm(forms.ModelForm):


    class Meta:
        model = TimeTable
        fields = ('name', 'description')




class EditTimeTableForm(forms.ModelForm):

    class Meta:
        model = TimeTable
        fields = ('name', 'description', 'owner')
