from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.

class EventView(viewsets.ModelViewSet) :
    queryset            = Event.objects.all()
    serializer_class    = EventSerializers

class CategoryView(viewsets.ModelViewSet) :
    queryset            = Category.objects.all()
    serializer_class    = CategorySerializers

class RegisterView(viewsets.ModelViewSet) :
    queryset            = Register.objects.all()
    serializer_class    = RegisterSerializers
