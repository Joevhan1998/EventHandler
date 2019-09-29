from rest_framework import serializers
from .models import *

class RegisterSerializers(serializers.ModelSerializer) :
    class Meta :
        model       = Register
        fields      = '__all__'


class CategorySerializers(serializers.ModelSerializer) :
    class Meta :
        model       = Category
        fields      = ('name', )

class EventSerializers(serializers.ModelSerializer) :
    category = CategorySerializers(many=True)
    class Meta :
        model       = Event
        fields      = '__all__'