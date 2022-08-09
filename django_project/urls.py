"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import index_view, images_view
from exercise.views import exercise_detail_view, exercise_create_view

urlpatterns = [
    path('', images_view, name='index'),
    path('create/', exercise_create_view, name='create'),
    path('detail/', exercise_detail_view, name='detail'),
    path('admin/', admin.site.urls),
    path('images/', images_view, name='images'),
]
