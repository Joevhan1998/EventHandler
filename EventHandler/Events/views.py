from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import *

class EventList(APIView):
    def get(self, request, format=None):
        request_data = request.GET.get("eventId", None)
        
        serializer = None
        if request_data is not None:
            try:
                pk = int(request_data)
                serializer = EventSerializers(Event.objects.filter(pk = pk), many = True)
            except ValueError:
                serializer = EventSerializers(Event.objects.none(), many = True)
        else:
                serializer = EventSerializers(Event.objects.none(), many = True)
        
        return Response(serializer.data)


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
        request_data = request.GET.get("categoryId", None)
        
        serializer = None
        if request_data is not None:
            try:
                pk = int(request_data)
                serializer = CategorySerializers(Category.objects.filter(pk = pk), many = True)
            except ValueError:
                serializer = CategorySerializers(Category.objects.none(), many = True)
        else:
                serializer = CategorySerializers(Category.objects.all(), many = True)
        return Response(serializer.data)

class RegisterList(APIView):
    def get(sefl, request, format = None):
        queryset = Register.objects.all()
        serializer = RegisterSerializers(queryset, many = True)
        return Response(serializer.data)

