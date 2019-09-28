'''
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.

""" class EventsView(viewsets.ModelViewSet) :
    queryset            = Event.objects.all()
    serializer_class    = EventSerializers
 """

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class EventList(APIView):
    def __init__(self):
        self.admin = False
    def get(self, request, format=None):
        if self.admin == True:
            events = Event.objects.all()
            serializer = EventSerializers(events, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        if self.admin == True:
            serializer = EventSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class EventDetail(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializers(event)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializers(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryView(viewsets.ModelViewSet) :
    queryset            = Category.objects.all()
    serializer_class    = CategorySerializers

class RegisterView(viewsets.ModelViewSet) :
    queryset            = Register.objects.all()
    serializer_class    = RegisterSerializers
'''


from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import *
from .models import *

class EventList(APIView):
    def __init__(self):
        self.admin = False
    def get(self, request, format=None):
        if self.admin == True:
            events = Event.objects.all()
            serializer = EventSerializers(events, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        if self.admin == True:
            serializer = EventSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class EventDetail(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializers(event)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializers(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryList(APIView):
    def get(self, request, format = None):
        queryset = Category.objects.all()
        serializer = CategorySerializers(queryset, many = True)
        print("REQUEST DATA", request.GET)
        return Response(serializer.data)

class RegisterList(APIView):
    def get(sefl, request, format = None):
        queryset = Register.objects.all()
        serializer = RegisterSerializers(queryset, many = True)
        return Response(serializer.data)

