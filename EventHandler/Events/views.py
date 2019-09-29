from rest_framework import viewsets
from rest_framework import filters
from .serializers import *
from .models import *

from rest_framework.filters import BaseFilterBackend
import coreapi

class SimpleFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='eventId',
            location='query',
            required=False,
            type='string'
        )]

class EventsView(viewsets.ModelViewSet) :
	# queryset = Event.objects.all()
	filter_backends = (SimpleFilterBackend,)
	serializer_class = EventSerializers
	# filter_backends = [filters.SearchFilter]
	# search_fields = ['name']
	
	def filter_queryset(self, queryset):
		return queryset

	def get_queryset(self):
		queryset = Event.objects.all()
		eventId = self.request.query_params.get('eventId', None)
		if eventId is not None:
			queryset = queryset.filter(pk=eventId)
		return queryset

class CategoryView(viewsets.ModelViewSet) :
    queryset            = Category.objects.all()
    serializer_class    = CategorySerializers

class RegisterView(viewsets.ModelViewSet) :
    queryset            = Register.objects.all()
    serializer_class    = RegisterSerializers
