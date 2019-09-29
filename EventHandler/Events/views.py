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
        	location='query',
        	required=False,
        	type='string' 
        ), coreapi.Field(
			name='search',
			location='query',
			required=False,
			type='string'
		),]

class RegisterFilterBackend(BaseFilterBackend):
	def get_schema_fields(self, view):
		return [coreapi.Field(
			name='eventId',
			location='query',
			required=False,
			type='string'
		),]

class EventsViewTime(viewsets.ModelViewSet) :
	serializer_class = EventSerializers

	def get_queryset(self):
		fromtime = self.kwargs['from_time']
		totime = self.kwargs['to_time']

		return Event.objects.all().filter(start_date_time__gte=fromtime).filter(end_date_time__lte=totime)

class EventsView(viewsets.ModelViewSet) :
	filter_backends = (EventFilterBackend,)
	serializer_class = EventSerializers

	def filter_queryset(self, queryset):
		return queryset

	def get_queryset(self):
		queryset = Event.objects.all()
		eventId = self.request.query_params.get('eventId', None)
		categoryId = self.request.query_params.get('categoryId', None)
		event_name = self.request.query_params.get('search', None)
		if eventId is not None:
			try:
				queryset = queryset.filter(pk=eventId)
			except ValueError:
				return None
		if categoryId is not None:
			queryset = queryset.filter(category__id=categoryId)
		if event_name is not None:
			queryset = queryset.filter(name__icontains=event_name)
		return queryset

class CategoryView(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializers

class RegisterView(viewsets.ModelViewSet):
	filter_backends = (RegisterFilterBackend,)
	serializer_class    = RegisterSerializers

	def get_queryset(self):
		queryset = Register.objects.all()
		eventId = self.request.query_params.get('eventId', None)

		if eventId is not None:
			queryset = queryset.filter(event_id__id=eventId)

		return queryset

	def filter_queryset(self, queryset):
		return queryset
