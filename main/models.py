from django.db import models

from main.enums import Zodiac


class Horoscope(models.Model):
    date = models.DateField(verbose_name='Date')
    zodiac = models.PositiveSmallIntegerField(choices=Zodiac.choices, verbose_name='Zodiac', unique_for_date='date')
    horoscope = models.TextField(verbose_name='Horoscope')
