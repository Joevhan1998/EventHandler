from rest_framework import serializers
from .models import *
from rest_framework.request import Request


class EventSerializers(serializers.ModelSerializer) :
    class Meta :
        model       = Event
        fields      = '__all__'
        #context     = {'request': Request(request)}

class RegisterSerializers(serializers.ModelSerializer) :
    class Meta :
        model       = Register
        fields      = '__all__'


class CategorySerializers(serializers.ModelSerializer) :
    class Meta :
        model       = Category
        fields      = '__all__'
