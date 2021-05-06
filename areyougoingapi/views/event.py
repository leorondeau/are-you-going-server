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
    class Meta:
        model = Goer
        fields = ['user']

class EventSerializer(serializers.HyperLinkedModelSerializer):

    class Meta:
        model = Event
        url = serializers.HyperlinkedIdentityField(
            view_name='event',
            lookup_field='id'
        )
        fields = ('id', 'goer', 'name', 'location', 'startDate',
        'details')