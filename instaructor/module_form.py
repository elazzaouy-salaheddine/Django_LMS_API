from django import forms
from course.models import Module

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['module_name', 'description','order']  # Specify the fields you want in the form

