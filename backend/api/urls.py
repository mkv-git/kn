from django.urls import path

from .views import ShipmentsListCreate, ShipmentsDetail


urlpatterns = [
    path('shipments/', ShipmentsListCreate.as_view(), name='shipments-list'),
    path('shipments/<int:pk>/', ShipmentsDetail.as_view(), name='shipments-detail')
]
