from django.forms import ModelForm
from pollapp.models import Polls
from django import forms

class PollForm(ModelForm):
    class Meta:
        model=Polls
        fields=["question","option_a","option_b","option_c"]
        widgets={
            'question':forms.Textarea(attrs={'class':'form-control','placeholder':'Post your question'}),
            'option_a': forms.TextInput(attrs={'class': 'form-control'}),
            'option_b': forms.TextInput(attrs={'class': 'form-control'}),
            'option_c': forms.TextInput(attrs={'class': 'form-control'})

        }


