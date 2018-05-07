from rest_framework import serializers
from .views import Team, Position

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class SalarySerializer(serializers.Serializer):
    descriptor = serializers.CharField(max_length=200)
    value_in_dollars = serializers.IntegerField()

