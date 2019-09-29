from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase, APIClient, RequestsClient
from .serializers import *
from .models import *
import json


class CategoryViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.initialized = False
        if (not self.initialized):
            Category.objects.create(name = "one")
            Category.objects.create(name = "two")
            Category.objects.create(name = "three")
            self.initialized = True

    def test_GET_all(self):
        response = self.client.get("/database/categories")
        expected = [value for value in Category.objects.all().values()]
        actual = json.loads(response.render().content)
        self.assertEqual(expected, actual)

    def test_GET_undefined(self):
        response = self.client.get("/database/categories", {"categoryId": 123})
        expected = [value for value in Category.objects.none().values()]
        actual = json.loads(response.render().content)
        self.assertEqual(expected, actual)

    def test_GET_1(self):
        response = self.client.get("/database/categories", {"categoryId": 1})
        expected = [value for value in Category.objects.filter(pk = 1).values()]
        actual = json.loads(response.render().content)
        self.assertEqual(expected, actual)

