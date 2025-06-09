from django.shortcuts import render
from rest_framework import generics

from .models import Shipments
from .paginator import Paginator
from .serializers import ShipmentsSerializer


class ShipmentsListCreate(generics.ListCreateAPIView):
    queryset = Shipments.objects.all()
    serializer_class = ShipmentsSerializer
    pagination_class = Paginator


class ShipmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipments.objects.all()
    serializer_class = ShipmentsSerializer
