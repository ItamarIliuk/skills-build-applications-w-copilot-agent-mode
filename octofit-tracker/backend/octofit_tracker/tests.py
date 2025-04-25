from django.test import TestCase
from .models import OctofitUser, Team, Activity, Workout, Leaderboard

class OctofitUserModelTest(TestCase):
    def test_create_user(self):
        user = OctofitUser.objects.create(email='test@example.com', name='Test User', password='123456')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = OctofitUser.objects.create(email='team@example.com', name='Team User', password='123456')
        team = Team.objects.create(name='Team A')
        team.members.add(user)
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = OctofitUser.objects.create(email='activity@example.com', name='Activity User', password='123456')
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, date='2025-04-25', points=10)
        self.assertEqual(activity.activity_type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', points=5)
        self.assertEqual(workout.name, 'Pushups')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = OctofitUser.objects.create(email='leader@example.com', name='Leader User', password='123456')
        leaderboard = Leaderboard.objects.create(user=user, total_points=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)
