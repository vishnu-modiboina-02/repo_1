from rest_framework import serializers
from .models import *

class CgargerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = charger
        fields = ['url','name','roll_no','email','address']