from rest_framework import viewsets
from .models import OctofitUser, Team, Activity, Workout, Leaderboard
from .serializers import OctofitUserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class OctofitUserViewSet(viewsets.ModelViewSet):
    queryset = OctofitUser.objects.all()
    serializer_class = OctofitUserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activity': '/api/activity/',
        'workouts': '/api/workouts/',
        'leaderboard': '/api/leaderboard/',
    })
