from django.test.client import encode_multipart
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json

URL = 'http://localhost:8000/api'

class AudioTests(APITestCase):
    def setUp(self):
        User.objects.create(username='gabozz', password='abcd1234*')

    def get_client(self):
        token = Token.objects.get(user__username='gabozz')

        client = APIClient()

        client.credentials(HTTP_AUTHORIZATION='Token %s' % token.key)

        return client

    def Test_post_group_audio(self):
        client = self.get_client()

        data = {
            'id': 1,
            'name': 'Nature',
            'is_available': True
        }

        req = client.post(URL + '/groupsaudios/', data, format='json')

        self.assertEqual(req.status_code, 201)

    def Test_get_group_audio(self):
        client = self.get_client()

        req = client.get(URL + '/groupsaudios/1/')

        self.assertEqual(json.loads(req.content), {'id': 1, 'name': 'Nature', 'is_available': True})

    def Test_post_audio(self):
        client = self.get_client()

        data = {
            'id': 1,
            'category': 1,
            'description': 'Beach',
            'is_available': True
        }

        req = client.post(URL + '/audios/', data, format='json')

        self.assertEqual(req.status_code, 201)

    def Test_get_audio(self):
        client = self.get_client()

        req = client.get(URL + '/audios/1/')

        self.assertEqual(json.loads(req.content), {'id': 1, 'category': 1, 'description': 'Beach', 'source': None, 'is_available': True})

    def Test_group_audio(self):
        self.Test_post_group_audio()
        self.Test_get_group_audio()

    def Test_audio(self):
        self.Test_post_audio()
        self.Test_get_audio()

    def tests(self):
        self.Test_group_audio()
        self.Test_audio()
