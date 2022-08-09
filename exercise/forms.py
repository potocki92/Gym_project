from .models import Exercises
from django import forms


class ExercisesFormModels(forms.ModelForm):
  class Meta:
    model = Exercises
    fields = [
      'title',
      'parts',
      'description'
    ]