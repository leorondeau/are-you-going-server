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
        events = Event.objects.filter(goer=goer)
        