from django.shortcuts import render

# Create your views here.
def slider_view(request):
  return render(request, "slider/images.html", {})