from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import *
from django.test import TestCase


class Pereval_addedTests(APITestCase):
    def setUp(self):

        self.user = Users.objects.create(email='testemail', phone='testphone', first_name='testuser1',
                                         last_name='testuser2', third_name='testuser3')

        self.coord = Coord.objects.create(latitude=1.0, longtude=2.0, height=2)

        self.level = Level.objects.create(winter='wintertest', summer='summertest', autumn='autumntest',
                                          spring='springtest')

        self.images = Pereval_images.objects.create(title='titletest', images='testimages.jpg')

        self.data = {
            'beutytitle': 'Test Beutytitle',
            'title': 'Test Title',
            'other_titles': 'Test Other_titles',
            'connect': 'Test Connect',
            'add_time': '2023-07-14 11:08:51',
            'user': self.user.pk,
            'coord': self.coord.pk,
            'level': self.level.pk,
            'images_test': self.images.pk,
            'status': 'new'
        }

    def test_create_pereval(self):
        url = reverse('submit_data')
        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pereval_added.objects.count(), 1)
        self.assertEqual(Pereval_added.objects.get().beutytitle, 'Test Beutytitle')

    def test_update_pereval(self):
        url = reverse('get_data', args=[1])
        response = self.client.patch(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Pereval_added.objects.count(), 1)
        self.assertEqual(Pereval_added.objects.get().beutytitle, 'Test Beutytitle')

