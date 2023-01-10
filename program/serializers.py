
from rest_framework import serializers
from .models import PassCode

class PassCodeSerializer(serializers.ModelSerializer):
    '''
    This Class Serializer helps validate passcode for a particular cource'''
    id = serializers.IntegerField()

    class Meta:
        model = PassCode
        fields = ('id', 'code')
    