import os

import requests
import datetime
import random

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from horoscope_back.settings import BASE_DIR
from main.enums import Zodiac
from main.models import Horoscope


def get_random_words() -> list:
    test_words_file = os.path.join(BASE_DIR, 'test_words_file.txt')
    if not os.path.exists(test_words_file):
        word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = requests.get(word_url, headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                          Chrome/87.0.4280.88 Safari/537.36'
        })
        long_txt = response.content.decode()
        with open(test_words_file,mode='w') as f:
            f.write(long_txt)
    with open(test_words_file) as f:
        long_txt = f.read()
    random_list = long_txt.splitlines()
    random.shuffle(random_list)
    return random_list


def fill_db_with_horoscopes():
    d = datetime.date(timezone.now().year, 1, 1)
    words = get_random_words()
    while d.year == timezone.now().year:
        for zodiac in Zodiac:
            r = random.randint(0, len(words) - 10)
            Horoscope.objects.get_or_create(
                date=d,
                zodiac=zodiac,
                horoscope=' '.join(words[r:r+10])
            )
        d += datetime.timedelta(days=1)


class HoroscopeTest(TestCase):

    def setUp(self) -> None:
        super().setUp()
        fill_db_with_horoscopes()

    def test_get_horoscope(self):
        response = self.client.get(reverse('get-horoscope-list', kwargs={'date': timezone.now().date()}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Horoscope.objects.filter(date=timezone.now().date()).count())

