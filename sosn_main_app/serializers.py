
from rest_framework import serializers
from .models import SubscribeNewsLetter

class SubscribeSerializer(serializers.ModelSerializer):
    '''
    This Class Serializer helps validate email for subscription'''

    class Meta:
        model = SubscribeNewsLetter
        fields = '__all__'
    