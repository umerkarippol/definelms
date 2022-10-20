from django import forms
from .models import *


class courseForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = course
        fields = ('course_name','description','amount','duration','exam','image','user')
class subjectForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = subject
        fields = ('subject_name','description','image','user')