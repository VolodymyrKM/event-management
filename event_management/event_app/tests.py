from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status


class UserViewSetTestCase(APITestCase):
    list_url = reverse("event-list")
    data = {
        "info": {
            "invitation": "100"
        },
        "timestamp": "2021-03-27T13:30:00.000000Z",
        "event_type": {
            "name": "Daughter birthday"
        }
    }

    def setUp(self):
        self.user = User.objects.create_user(username='davinchi',
                                             password='some-vey-strong-psw')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.client.post(self.list_url, self.data, format='json')

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_event_list_ok_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_list_invalid_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_creation_event_good(self):
        event_party = {
            "info": {
                "invitation": "150"
            },
            "timestamp": "2021-03-27T13:49:51.141000Z",
            "event_type": {
                "name": "Dance Party"
            }}
        response = self.client.post(self.list_url, event_party, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_creation_event_invalid(self):
        event_party = {
            "info": {
                "invitation": 340
            },
            "timestamp": "2018-12-10T13:49:51.141000Z",
            "event_type": {
                "name": None
            }}
        response = self.client.post(self.list_url, event_party, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
