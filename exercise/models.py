from django.db import models

# Create your models here.
part_of_exercise = (
  ('klatka','KLATKA'),
  ('nogi','NOGI'),
  ('barki','BARKI'),
)

class Exercises(models.Model):

  title = models.CharField(max_length = 100, verbose_name='Nowy tytuł')
  description = models.TextField(blank = True, null = True, verbose_name = 'Opis', help_text='opisz co to za ćwiczenie')
  parts = models.CharField(max_length=10, choices = part_of_exercise, verbose_name='Partie trenowane', help_text='wybierz z listy')
  featured = models.BooleanField(default = True)