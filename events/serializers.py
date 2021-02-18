from rest_framework import serializers

from .models import Sports_Events
from .models import Cultural_Events
from .models import Technical_Events

class Sports_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sports_Events
        fields = '__all__'

class Cultural_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cultural_Events
        fields = '__all__'

class Technical_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Technical_Events
        fields = '__all__'