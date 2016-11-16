from django import forms
from django.forms import Textarea

from .models import Comment


class CreateCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {
            'text': Textarea(attrs={'cols':5, 'rows':2, 'value': "Comment"})
        }
        initial = {
            'text': "commnet"
        }
