from django import forms
from django.forms import ModelForm
from .models import Task

# This class creates forms tied to the "Task" model including all the fields using the "ModelForm"
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"  # include all fields in form. fields=('title','completed')