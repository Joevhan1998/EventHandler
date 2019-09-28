from rest_framework import serializers
from .models import Category

"""
class EventSerializers(serializers.HyperLinkedModelSerializer) :
    class Meta :
        model       = Event
        fields      = '__all__'

class RegisterSerializers(serializers.HyperLinkedModelSerializer) :
    class Meta :
        model       = Register
        fields      = '__all__'
"""

class CategorySerializers(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model       = Category
        fields      = '__all__'
