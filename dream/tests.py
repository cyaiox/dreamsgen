from django.test.client import encode_multipart
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from audio.tests import AudioTests
import json

URL = 'http://localhost:8000/api'


class DreamTests(APITestCase):
    def setUp(self):
        User.objects.create(username='gabozz', password='abcd1234*')

    def get_client(self):
        token = Token.objects.get(user__username='gabozz')

        client = APIClient()

        client.credentials(HTTP_AUTHORIZATION='Token %s' % token.key)

        return client

    def Test_post_group_dream(self):
        client = self.get_client()

        data = {
            'id': 1,
            'name': 'Sci-Fi',
            'is_available': True
        }

        req = client.post(URL + '/groupsdreams/', data, format='json')

        self.assertEqual(req.status_code, 201)

    def Test_get_group_dream(self):
        client = self.get_client()

        req = client.get(URL + '/groupsdreams/1/')

        self.assertEqual(json.loads(req.content), {'id': 1, 'name': 'Sci-Fi', 'is_available': True})

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

        data = {
            'id': 1,
            'category': 1,
            'description': 'Beach',
            'source': None,
            'is_available': True
        }

        self.assertEqual(json.loads(req.content), data)

    def Test_post_dream(self):
        client = self.get_client()

        data = {
            'id': 1,
            'name': 'Interstellar',
            'description': 'A sci-fi tale',
            'introduction': 'A sci-fi tale',
            'is_available': True,
            'price': 2.0,
            'alarm_sound': 1,
            'alarm_time': 90,
            'alarm_duration': 120,
            'alarm_repetition': 4,
            'dream_sound': 1,
            'group': 1
        }

        content = encode_multipart('BoUnDaRyStRiNg', data)

        content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'

        req = client.post(URL + '/dreams/', content, content_type=content_type)

        self.assertEqual(req.status_code, 201)

    def Test_get_dream(self):
        client = self.get_client()

        data = {
            'id': 1,
            'name': 'Interstellar',
            'description': 'A sci-fi tale',
            'introduction': 'A sci-fi tale',
            'cover_page': None,
            'is_available': True,
            'price': 2.0,
            'alarm_sound': 1,
            'alarm_time': 90,
            'alarm_duration': 120,
            'alarm_repetition': 4,
            'dream_sound': 1,
            'group': 1,
            'android_code': None,
            'ios_code': None,
            'frames': []
        }

        req = client.get(URL + '/dreams/1/')

        self.assertEqual(json.loads(req.content), data)

    def Test_group_audio(self):
        self.Test_post_group_audio()
        self.Test_get_group_audio()

    def Test_audio(self):
        self.Test_post_audio()
        self.Test_get_audio()

    def Test_group_dream(self):
        self.Test_post_group_dream()
        self.Test_get_group_dream()

    def Test_dream(self):
        self.Test_post_dream()
        self.Test_get_dream()

    def tests(self):
        self.Test_group_audio()
        self.Test_audio()
        self.Test_group_dream()
        self.Test_dream()
