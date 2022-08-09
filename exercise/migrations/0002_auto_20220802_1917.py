# Generated by Django 3.2.13 on 2022-08-02 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='description',
            field=models.TextField(blank=True, help_text='opisz co to za ćwiczenie', null=True, verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='exercises',
            name='parts',
            field=models.CharField(choices=[('klatka', 'KLATKA'), ('nogi', 'NOGI'), ('barki', 'BARKI')], help_text='wybierz z listy', max_length=10, verbose_name='Partie trenowane'),
        ),
        migrations.AlterField(
            model_name='exercises',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Nowy tytuł'),
        ),
    ]