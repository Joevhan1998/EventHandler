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
        response = self.client.get("/categories/")
        print(response)
        expected = [value for value in Category.objects.all().values()]
        print(expec)
        actual = json.loads(response.render().content)
        self.assertEqual(expected, actual)

    def test_GET_undefined(self):
        response = self.client.get("/categories/123/")
        assert response.status_code == 404

    def test_GET_2(self):
        response = self.client.get("/categories/2/")
        expected = [value for value in Category.objects.filter(pk = 2).values()]
        actual = [json.loads(response.render().content)]
        self.assertEqual(expected, actual)
"""
    def test_POST(self):
        response = self.client.post("/categories", headers = {"Authorization": "Bearer sometoken"}, data = {"name": "four"})
        assert None != Category.objects.filter(name = "four")

    def test_PUT_3(self):
        response = self.client.put("/categories", headers = {"Authorization": "Bearer sometoken"}, data = {"categoryId": 3, "name": "four"})
        expected = {"categoryId": 3, "name": "four"}
        actual = Category.objects.filter(name = "four").first()
        actual = {"categoryId": actual.pk, "name": actual.name}
        self.assertEqual(expected, actual)

    def test_DELETE_4(self):
        response = self.client.delete("/categories", headers = {"Authorization": "Bearer sometoken"}, data = {"categoryId": 4})
        for pair in Category.objects.all():
            assert (pair.pk != 4)
"""

class EventViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.initialized = False
        if (not self.initialized):
            category1 = Category.objects.create(name = "category1")
            category2 = Category.objects.create(name = "category2")
            Event.objects.create(name = "event1", start_date_time = "2019-12-20T10:00:00+0100", end_date_time = "2019-12-21T10:00:00+0100", max_participants = 50, min_participants = 20, descriptions = "event1 description", status = "O", category = category1, organizer_name = "Org1")
            Event.objects.create(name = "event2", start_date_time = "2019-12-24T10:00:00+0100", end_date_time = "2019-12-25T10:00:00+0100", max_participants = 60, min_participants = 10, descriptions = "event2 description", status = "C", category = category1, organizer_name = "Org2")
            Event.objects.create(name = "event2", start_date_time = "2019-12-26T10:00:00+0100", end_date_time = "2019-12-27T10:00:00+0100", max_participants = 70, min_participants = 0, descriptions = "event3 description", status = "O", category = category2, organizer_name = "Org3")
            self.initialized = True
    def test_GET_search_2(self):
        response = self.client.get("/events/", data = {"search": "event2"})
        response.json.loads(response.render().content)
        self.assertEqual(len(response), 2)
    
    def test_GET_search_undefined(self):
        response = self.client.get("/events/", data = {"search": "event22e1casc"})
        assert(404 == response.status_code)

    def test_GET_time(self):
        response = self.client.get("/events/2019-12-19T10:00:00+0100/2019-12-22T10:00:00+0100/")
        response = json.loads(response.render().content)

        response = {"eventName": response.eventName}
        expected = {"eventName": "event1"}

        self.assertEqual(response, expected)

    def test_GET_time_undefined(self):
        response = self.client.get("/events/2018-12-19T10:00:00+0100/2018-12-22T10:00:00+0100/")
        assert(404 == response.status_code)

    def test_GET_category(self):
        response = self.client.get("/events/", data = {"categoryId": 2})
        response = json.loads(response.render().content)
        
        response = {"eventName": response.eventName}
        expected = {"eventName": "event3"}

        self.assertEqual(response, expected)


    def test_GET_3(self):
        response = self.client.get("/events/", data = {"eventId": 3})
        response = json.loads(response.render().content)
        response = {"eventId": response.pk, "name": response.name}

        expected = Category.objects.filter(pk = 3)
        expected = {"eventId": expected.pk, "name": expected.name}
        
        self.assertEqual(response, expected)

    def test_GET_undefined(self):
        response = self.client.get("/events/", data = {"eventId": "23aca"})
        self.assertEqual(404, response.status_code)

    def test_POST_admin(self):
        response = self.client.post("/events/", header = {"Authorization": "Bearer ..acasc"}, data = {"eventName": "event4", "startDateTime": "2019-12-23T10:00:00+0100", "endDateTime": "2019-12-23T10:00:00+0100", "maxParticipants": 50, "minParticipants": 20, "organizerName": "some org", "descriptions": "some description", "categoryId": 3, "eventStatus": "C"})
        self.assertEqual(201, response.status_code)
        expected = Event.objects.filter(name = "event4")
        assert (0 != len(expected))
    
    def test_POST(self):
        response = self.client.post("/events/", data = {"eventName": "event4", "startDateTime": "2019-12-23T10:00:00+0100", "endDateTime": "2019-12-23T10:00:00+0100", "maxParticipants": 50, "minParticipants": 20, "organizerName": "some org", "descriptions": "some description", "categoryId": 3, "eventStatus": "C"})
        self.assertEqual(401, response.status_code)

    def test_DELETE_admin(self):
        response = self.client.delete("/events/", header = {"Authorization": "Bearer ..acasc"}, data = {"eventId": 1})
        self.assertEqual(201, response.status_code)
        expected = Event.objects.filter(pk = 1)
        assert (0 == len(expected))
    
    def test_DELETE(self):
        response = self.client.delete("/events/",  data = {"eventId": 1})
        self.assertEqual(401, response.status_code)

    def test_PUT_admin(self):
        response = self.client.put("/events/", header = {"Authorization": "Bearer ..acasc"}, data = {"eventId": 1, "eventName": "event20", "startDateTime": "2019-12-20T10:00:00+0100", "endDateTime": "2019-12-20T10:00:00+0100", "maxParticipants": 30, "minParticipants": 0, "organizerName": "noname", "descriptions": "whatever description"})
        response = {"eventName": response.EventName}
        self.assertEqual(200, response.status_code)
        expected = Event.objects.filter(pk = 1)
        expected = {"eventName": expected.eventName}
        self.assertEqual(expected, response)

    def test_PUT(self):
        response = self.client.put("/events/", data = {"eventId": 1, "eventName": "event20", "startDateTime": "2019-12-20T10:00:00+0100", "endDateTime": "2019-12-20T10:00:00+0100", "maxParticipants": 30, "minParticipants": 0, "organizerName": "noname", "descriptions": "whatever description"})
        self.assertEqual(401, response.status_code)

class RegisterViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.initialized = False
        if (not self.initialized):

            c1 = Category.objects.create(name = "category1")
            c2 = Category.objects.create(name = "category2")
            
            e1 = Event.objects.create(name = "event1", start_date_time = "2019-12-20T10:00:00+0100", end_date_time = "2019-12-21T10:00:00+0100", max_participants = 50, min_participants = 20, descriptions = "event1 description", status = "O", category = c1, organizer_name = "Org1")
            e2 = Event.objects.create(name = "event2", start_date_time = "2019-12-24T10:00:00+0100", end_date_time = "2019-12-25T10:00:00+0100", max_participants = 60, min_participants = 10, descriptions = "event2 description", status = "C", category = c2, organizer_name = "Org2")
            e3 = Event.objects.create(name = "event2", start_date_time = "2019-12-26T10:00:00+0100", end_date_time = "2019-12-27T10:00:00+0100", max_participants = 70, min_participants = 0, descriptions = "event3 description", status = "O", category = c1, organizer_name = "Org3")

            r1 = Register.objects.create(event_id = e1, participant_id = 3, attendance = True, feedback = "somefeedback")
            r2 = Register.objects.create(event_id = e1, participant_id = 2, attendance = False, feedback = "")

        def test_POST(self):
            response = self.client.post("/events/volunteer/", data = {"eventId": 1, "userId": 5})
            expected = Register.objects.filter(eventId = 1, userId = 5)
            self.assertEqual(1, expected)
        
        def test_DELETE(self):
            response = self.client.delete("/events/volunteer/", data = {"eventId": 1, "userId": 5})
            expected = Register.objects.filter(eventId = 1, userId = 5)
            self.assertEqual(0, expected)

        def test_GET_allfeedback(self):
            response = self.client.get("/events/feedback/", data = {"eventId": 1})
            expected = Register.objects.filter(eventId = 1)
            print(expected)

        def test_GET_feedback(self):
            response = self.client.get("/events/feedback/", data = {"registerId": 1})
            expected = Register.objects.filter(registerId = 1)
            pront(expected)




            self.initialized = True