from django.shortcuts import render
from .models import Exercises

from .forms import ExercisesFormModels

# Create your views here.
def exercise_create_view(request):
  form = ExercisesFormModels(request.POST or None)
  if form.is_valid():
    form.save()

  context = {
    'form' : form
  }
  return render(request, 'exercise/exercise_create.html', context)

def exercise_detail_view(request):

  obj = Exercises.objects.all()

  context = {
    'object' : obj
  }
  return render(request, 'exercise/exercise_detail.html', context)