from django import forms
from .models import Resource_Model


class ResourceForm(forms.ModelForm):
  class Meta:
    model = Resource_Model
    fields = '__all__'