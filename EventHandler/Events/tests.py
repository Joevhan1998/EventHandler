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
        response = self.client.get("/database/categories", data = {"categoryId": 123})
        expected = [value for value in Category.objects.none().values()]
        actual = json.loads(response.render().content)
        self.assertEqual(expected, actual)

    def test_GET_2(self):
        response = self.client.get("/database/categories", data = {"categoryId": 2})
        expected = [value for value in Category.objects.filter(pk = 2).values()]
        actual = json.loads(response.render().content)
        self.assertEqual(expected, actual)

    def test_POST(self):
        response = self.client.post("/database/categories", headers = {"Authorization": "Bearer sometoken"}, data = {"name": "four"})
        assert None != Category.objects.filter(name = "four")

    def test_PUT_3(self):
        response = self.client.put("/database/categories", headers = {"Authorization": "Bearer sometoken"}, data = {"categoryId": 3, "name": "four"})
        expected = {"categoryId": 3, "name": "four"}
        actual = Category.objects.filter(name = "four").first()
        actual = {"categoryId": actual.pk, "name": actual.name}
        self.assertEqual(expected, actual)

    def test_DELETE_4(self):
        response = self.client.delete("/database/categories", headers = {"Authorization": "Bearer sometoken"}, data = {"categoryId": 4})
        for pair in Category.objects.all():
            assert (pair.pk != 4)


