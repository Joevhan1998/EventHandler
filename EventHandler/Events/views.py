from rest_framework import viewsets
from .serializers import CategorySerializers
from .models import Category
# Create your views here.
"""
class EventsView(viewsets.ModelViewSet) :
    queryset        = Event.objects.all()
"""

class CategoryView(viewsets.ModelViewSet) :
    queryset            = Category.objects.all()
    serializer_class    = CategorySerializers
