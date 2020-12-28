from django.urls import path

from main.views import HoroscopeListView, HoroscopeDetailView

urlpatterns = [
    path('horoscope/<str:date>/', HoroscopeListView.as_view(), name='get-horoscope-list'),
    path('horoscope/<str:date>/<str:zodiac>', HoroscopeDetailView.as_view(), name='get-horoscope-detail'),
]