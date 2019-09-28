from rest_framework import serializers
from .models import *


class EventSerializers(serializers.ModelSerializer) :
    class Meta :
        model       = Event
        fields      = '__all__'

class RegisterSerializers(serializers.ModelSerializer) :
    class Meta :
        model       = Register
        fields      = '__all__'


class CategorySerializers(serializers.ModelSerializer) :
    class Meta :
        model       = Category
        fields      = '__all__'
