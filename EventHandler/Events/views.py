from rest_framework import viewsets
from rest_framework import filters
from .serializers import *
from .models import *

from rest_framework.filters import BaseFilterBackend
import coreapi

class EventFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='eventId',
            location='query',
            required=False,
            type='string'
        ), coreapi.Field(
        	name='categoryId',
        	Location='query',
        	required=False,
        	type='string' 
        )]

class EventsViewSearch(viewsets.ModelViewSet) :
	queryset = Event.objects.all()
	serializer_class = EventSerializers
	filter_backends = (filters.SearchFilter,)
	search_fields = ['name']

class EventsView(viewsets.ModelViewSet) :
	# queryset = Event.objects.all()
	filter_backends = (EventFilterBackend,)
	serializer_class = EventSerializers
	# filter_backends = [filters.SearchFilter]
	
	def filter_queryset(self, queryset):
		return queryset

	def get_queryset(self):
		queryset = Event.objects.all()
		eventId = self.request.query_params.get('eventId', None)
		categoryId = self.request.query_params.get('categoryId', None)
		if eventId is not None:
			queryset = queryset.filter(pk=eventId)
		if categoryId is not None:
			queryset = queryset.filter(category__id=categoryId)
		return queryset

class CategoryView(viewsets.ModelViewSet) :
    queryset            = Category.objects.all()
    serializer_class    = CategorySerializers

class RegisterView(viewsets.ModelViewSet) :
    queryset            = Register.objects.all()
    serializer_class    = RegisterSerializers
