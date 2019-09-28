from rest_framework import viewsets
from rest_framework import filters
from .serializers import *
from .models import *

class EventsView(viewsets.ModelViewSet) :
	queryset = Event.objects.all()
	serializer_class = EventSerializers
	filter_backends = [filters.SearchFilter]
	search_fields = ['name']

class CategoryView(viewsets.ModelViewSet) :
    queryset            = Category.objects.all()
    serializer_class    = CategorySerializers

class RegisterView(viewsets.ModelViewSet) :
    queryset            = Register.objects.all()
    serializer_class    = RegisterSerializers
