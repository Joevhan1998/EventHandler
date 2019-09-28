from rest_framework import serializers
from .models import *


class EventSerializers(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model       = Event
        fields      = '__all__'

class RegisterSerializers(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model       = Register
        fields      = '__all__'


class CategorySerializers(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model       = Category
        fields      = '__all__'
