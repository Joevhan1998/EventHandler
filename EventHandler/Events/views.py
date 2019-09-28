'''
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.

class EventsView(viewsets.ModelViewSet) :
    queryset            = Event.objects.all()
    serializer_class    = EventSerializers

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

class EventsList(APIView):
    def get(self, request, format = None):
        queryset = Event.objects.all()
        serializer = EventSerializers(queryset, many = True)
        return Response(serializer.data)

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

