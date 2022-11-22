from django import forms
from django.forms import fields, widgets
from django.forms.models import ModelForm
from .models import *


class designationForm(forms.ModelForm):
    class Meta:
        model = designation
        fields = ['designation']
        widgets = {
            'designation': forms.TextInput(attrs={'class':'form-control', 'id':'desigantionid'}),

        }
