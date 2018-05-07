from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Team, Position
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
        queryset = self.get_queryset()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        if self.request.GET['team_name'] and Team.objects.filter(name_abbreviated=self.request.GET['team_name'].upper()):
            return Team.objects.filter(name_abbreviated=self.request.GET['team_name'].upper())

        return Team.objects.all()
        


class ListSalariesByPosition(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = SalarySerializer
