from django.shortcuts import render
from rest_framework import generics

from .models import Shipments
from .serializers import ShipmentsSerializer


class ShipmentsListCreate(generics.ListCreateAPIView):
    queryset = Shipments.objects.all()
    serializer_class = ShipmentsSerializer


class ShipmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipments.objects.all()
    serializer_class = ShipmentsSerializer
