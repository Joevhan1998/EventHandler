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
			type='string',
		)]

class RegisterFilterBackend(BaseFilterBackend):
	def get_schema_fields(self, view):
		return [coreapi.Field(
			name='eventId',
			location='query',
			required=False,
			type='string',
		)]

class EventsView(viewsets.ModelViewSet) :
	filter_backends = (EventFilterBackend,)
	serializer_class = EventSerializers

	def list(self, request, *args, **kwargs):
		response = super(EventsView, self).list(request, *args, **kwargs)
		response.data = {"events": response.data}
		return response

	def filter_queryset(self, queryset):
		return queryset

	def get_queryset(self):
		queryset = Event.objects.all()
		eventId = self.request.query_params.get('eventId', None)
		categoryId = self.request.query_params.get('categoryId', None)
		event_name = self.request.query_params.get('search', None)
		if eventId is not None:
			queryset = queryset.filter(pk=eventId)
		if categoryId is not None:
			queryset = queryset.filter(category__id=categoryId)
		if event_name is not None:
			queryset = queryset.filter(name__icontains=event_name)
		return queryset

class CategoryView(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializers
	def list(self, request, *args, **kwargs):
		response = super(CategoryView, self).list(request, *args, **kwargs)
		response.data = {"categories": response.data}
		return response

class RegisterView(viewsets.ModelViewSet):
	filter_backends = (RegisterFilterBackend,)
	serializer_class    = RegisterSerializers

	def list(self, request, *args, **kwargs):
		response = super(RegisterView, self).list(request, *args, **kwargs)
		response.data = {"registers": response.data}
		return response

	def get_queryset(self):
		queryset = Register.objects.all()
		eventId = self.request.query_params.get('eventId', None)

		if eventId is not None:
			queryset = queryset.filter(event_id__id=eventId)

		return queryset

	def filter_queryset(self, queryset):
		return queryset
