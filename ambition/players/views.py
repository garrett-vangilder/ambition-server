from django.shortcuts import render, get_object_or_404
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


class ListSalariesByPosition(viewsets.ViewSet):
    serializer_class = SalarySerializer

    def list(self, request):
        payload = []
        team_entity = None
        
        # team entity lookup
        if self.request.GET.get('team_name'):
            team = get_object_or_404(Team,
                name_abbreviated=self.request.GET.get('team_name').upper())
            team_entity = Entity.objects.get_for_obj(team)

        # loop through positions
        for position in Position.objects.all():

            position_entity = Entity.objects.get_for_obj(Position.objects.get(name=position.name))

            # if there is a team then get intersection of team and position
            if team_entity:
                player_entities = set(position_entity.get_super_entities()) & set(team_entity.get_super_entities())
            else:
                player_entities = position_entity.get_super_entities()
            
            # figure out average salary
            salary = 0
            if len(player_entities) >= 1:
                for player in player_entities:
                    salary = salary + int(player.entity_meta['salary'])
                
                average = salary / len(player_entities)
                value_in_dollars = round(average, 2)

                # serialize
                salary = SalarySerializer(data={'description': position.name, 'value_in_dollars': value_in_dollars})

                # validate
                salary.is_valid()

                # append to route payload
                payload.append(salary.data)
        
        return Response(payload)


class ListSalariesByTeam(viewsets.ViewSet):
    serializer_class = SalarySerializer

    def list(self, request):
        payload = []
        position_entity = None

        # position entity lookup
        if self.request.GET.get('position_name'):
            position = get_object_or_404(Position,
                                     name_abbreviated=self.request.GET.get('position_name').upper())
            position_entity = Entity.objects.get_for_obj(position)

        # loop through teams
        for team in Team.objects.all():

            team_entitiy = Entity.objects.get_for_obj(
                Team.objects.get(name=team.name))

            # if there is a team then get intersection of team and position
            if position_entity:
                player_entities = set(team_entitiy.get_super_entities()) & set(
                    position_entity.get_super_entities())
            else:
                player_entities = team_entitiy.get_super_entities()

            # figure out average salary
            salary = 0
            if len(player_entities) >= 1:
                for player in player_entities:
                    salary = salary + int(player.entity_meta['salary'])

                average = salary / len(player_entities)
                value_in_dollars = round(average, 2)

                # serialize
                salary = SalarySerializer(
                    data={'description': team.name, 'value_in_dollars': value_in_dollars})

                # validate
                salary.is_valid()

                # append to route payload
                payload.append(salary.data)

        return Response(payload)
