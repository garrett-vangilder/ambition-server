from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType

from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from entity.models import Entity

from .models import Team, Position, Player
from .serializers import TeamSerializer, SalarySerializer


class ListTeamsName(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ListPositionsName(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = TeamSerializer


class ListSalariesByTeam(viewsets.ViewSet):
    serializer_class = SalarySerializer

    def list(self, request):
        payload = []
        
        # team entity lookup
        team_entity = Entity.objects.get_for_obj(Team.objects.get(
            name_abbreviated=self.request.GET.get('team_name').upper()))
        
        # TODO: Update for when a team is selected
        if self.request.GET.get('team_name') == None:

            for position in Position.objects.all():

                position_entity = Entity.objects.get_for_obj(Position.objects.get(name=position.name))
                player_entities = position_entity.get_super_entities()
                salary = 0
                for player in player_entities:
                    salary = salary + int(player.entity_meta['salary'])
                payload.append({ position.name : round((salary / len(player_entities)), 2)  })
        
        return Response(payload)


class ListSalariesByPosition(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = SalarySerializer
