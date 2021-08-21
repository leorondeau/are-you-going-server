from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from areyougoingapi.models import Goer
from areyougoingapi.models import Event


class Goers(ViewSet):
    def list(self, request):

        goers = Goer.objects.all()
        # events = Event.objects.all()

        serializer = GoerSerializer(
            goers, many=True, context={'request': request})
        return Response(serializer.data)

class GoerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goer
        url = serializers.HyperlinkedIdentityField(
            view_name='goer',
            lookup_field='id'
        )
        fields = ('id', 'user')


