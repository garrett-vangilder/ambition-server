from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Team
from .serializers import TeamSerializer


class ListTeamsName(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
