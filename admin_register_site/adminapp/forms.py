from django import forms
from .models import *
from . import services

# faculty
class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }



# kafedra
class KafedraForm(forms.ModelForm):
    class Meta:
        model = Kafedra
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }



# groups
class GroupsForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }


# students
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }

# subject
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }


# teachers
class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }