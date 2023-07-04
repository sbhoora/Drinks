from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta: #meta data describing the model, which is 'drink'
        model = Drink
        fields = ['id','name','description'] #list of all the fields of the model