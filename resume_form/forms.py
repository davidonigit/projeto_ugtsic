from django import forms
from .models import ResumeSubmit

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeSubmit
        fields = ['name', 'email', 'celphone', 'position', 'education', 'observations', 'file']