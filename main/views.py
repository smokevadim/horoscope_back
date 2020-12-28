from django.shortcuts import get_list_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from main.models import Horoscope
from main.serializers import HoroscopeSerializer, HoroscopeDetailSerializer


class HoroscopeListView(generics.GenericAPIView):
    serializer_class = HoroscopeSerializer

    def get(self, request, *args, **kwargs):
        instance = get_list_or_404(Horoscope.objects.all(), date=kwargs['date'])
        data = HoroscopeSerializer(instance, context={'request': request}, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class HoroscopeDetailView(generics.GenericAPIView):
    serializer_class = HoroscopeDetailSerializer

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(Horoscope.objects.all(), date=kwargs['date'], zodiac=kwargs['zodiac'])
        data = HoroscopeSerializer(instance, context={'request': request}, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)