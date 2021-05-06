from re import S
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from areyougoingapi.models import Event
from areyougoingapi.models import Goer

class Events(ViewSet):
    def create(self, request):

        goer = Goer.objects.get(user=request.auth.user)

        event = Event()
        event.name = request.data["name"]
        event.location = request.data["location"]
        event.startDate = request.data["startDate"]
        event.details = request.data["details"]
        event.goer = goer

        try:
            event.save()
            serializer = EventSerializer(event, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request):

        goer = Goer.objects.get(user=request.auth.user)
        events = Event.objects.all()

        serializer = EventSerializer(
            events, many=True, context={'request': request})
        return Response(serializer.data)


class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class EventGoerSerializer(serializers.ModelSerializer):
    user = EventUserSerializer(many=False)

    class Meta:
        model = Goer
        fields = ['user']

class EventSerializer(serializers.HyperlinkedModelSerializer):

    goer = EventGoerSerializer(many=False)
    
    class Meta:
        model = Event
        url = serializers.HyperlinkedIdentityField(
            view_name='event',
            lookup_field='id'
        )
        fields = ('id', 'goer', 'name', 'location', 'startDate',
        'details')