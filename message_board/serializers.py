from rest_framework import serializers
from .models import Board, Message

class BoardSerialiser(serializers.ModelSerializer):
    
    class Meta:
        model = Board
        fields = '__all__'


class MessageSerialiser(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = '__all__'