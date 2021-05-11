from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from areyougoingapi.models import Goer
from areyougoingapi.models import Event


class Profile(ViewSet):

    def list(self, request):

        goer = Goer.objects.get(user=request.auth.user)
        events = Event.objects.filter(goer =  goer)
        
        events = EventSerializer( events, many=True, context={'request': request})
        goer = GoerSerializer( goer, many = False, context={'request': request})

        profile = {}
        profile["goer"] = goer.data
        profile["events"] = events.data

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']

class GoerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Goer
        fields = ['user']

class EventSerializer(serializers.ModelSerializer):
    goer = GoerSerializer(many=False)

    class Meta:
        model = Event
        fields = ['id', 'goer' , 'name', 'location', 'startDate', 'details']

        
    
