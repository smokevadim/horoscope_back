from rest_framework import serializers

from main.enums import Zodiac
from main.models import Horoscope


class HoroscopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horoscope
        fields = ['zodiac', 'horoscope']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['zodiac'] = Zodiac.choices[ret['zodiac']-1][1]
        return ret


class HoroscopeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horoscope
        fields = ['horoscope']