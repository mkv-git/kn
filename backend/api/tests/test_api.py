import datetime

import pytz
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Shipments


DEFAULT_TIMEZONE = "Europe/Tallinn"


class ShipmentsTests(APITestCase):

    def test_create_shipment(self):
        """
        Ensure we can create a new shipment object.
        """
        url = reverse('shipments-list')
        data = {
            's_name': 'test',
            's_start_ts': datetime.datetime.now(tz=pytz.timezone('Europe/Tallinn')),
            's_from': 'tartu',
            's_to': 'tallinn',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shipments.objects.count(), 1)
        self.assertEqual(Shipments.objects.get().s_name, 'test')

    def test_required_fiels(self):
        url = reverse('shipments-list')
        data = {}
        expected_error_obj = {
            's_name': ['This field is required.'],
            's_start_ts': ['This field is required.'],
            's_from': ['This field is required.'],
            's_to': ['This field is required.']
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Shipments.objects.count(), 0)
        self.assertEqual(response.json(), expected_error_obj)

    def test_from_to(self):
        """ Shipments source and destinations can't be the same
        """

        url = reverse('shipments-list')
        data = {
            's_name': 'test',
            's_start_ts': datetime.datetime.now(tz=pytz.timezone('Europe/Tallinn')),
            's_from': 'tartu',
            's_to': 'tartu',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Shipments.objects.count(), 0)
        self.assertEqual(response.json().get('non_field_errors', []), ['Shipment source and destination are the same!'])

    def test_shipment_timestamps(self):
        now = datetime.datetime.now(tz=pytz.timezone('Europe/Tallinn'))

        url = reverse('shipments-list')        
        data = {
            's_name': 'test',
            's_start_ts': now,
            's_end_ts': now - datetime.timedelta(hours=1),
            's_from': 'tartu',
            's_to': 'tallinn',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Shipments.objects.count(), 0)
        self.assertEqual(response.json().get('non_field_errors', []), ['Shipment start timestamp must be lower than end timestamp'])

