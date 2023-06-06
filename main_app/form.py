from django.forms import ModelForm
from .models import Child

class ChildForm(ModelForm):
  class Meta:
    model = Child
    fields = ['date', 'meal']