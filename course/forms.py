from django.utils.translation import ugettext as _
from django import forms 
from pagedown.widgets import AdminPagedownWidget

from .models import *



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name"]
    


class ModuleForm(forms.ModelForm):
    description = forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Module
        fields = ["name", "description", "course"]
