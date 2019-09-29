from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase, APIClient, RequestsClient
from .serializers import *
from .models import *
import json


class BaseViewTest(APITestCase):
    def setUp(self):
        #self.client = RequestsClient()
        self.client = APIClient()


class CategoryViewTest(BaseViewTest):
    def setUp(self):
        super().setUp()
        #Category.objects.create(name = "one")
        #Category.objects.create(name = "two")
        #Category.objects.create(name = "three")

    def test_GET_all(self):
        response = self.client.get("/database/categories")
        expected = [value for value in Category.objects.all().values()]
        actual = json.loads(response.render().content)
        self.assertEqual(expected, actual)

    def test_GET_undefined(self):
        response = self.client.get("/database/categories", {"categoryId": 123})
        expected = [value for value in Category.objects.all().values()]
        actual = json.loads(response.render().content)
        self.assertEqual(expected, actual)


