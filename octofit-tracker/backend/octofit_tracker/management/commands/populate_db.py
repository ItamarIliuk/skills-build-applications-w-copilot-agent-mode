from django.core.management.base import BaseCommand
from octofit_tracker.models import OctofitUser, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Popula o banco octofit_db com dados de teste para users, teams, activities, leaderboard e workouts.'

    def handle(self, *args, **kwargs):
        # Usuários
        alice = OctofitUser.objects.create(email='alice@octofit.com', name='Alice', password='alicepass')
        bob = OctofitUser.objects.create(email='bob@octofit.com', name='Bob', password='bobpass')
        carol = OctofitUser.objects.create(email='carol@octofit.com', name='Carol', password='carolpass')

        # Times (usando lista de emails)
        team1 = Team.objects.create(name='Team Alpha', members=[alice.email, bob.email])
        team2 = Team.objects.create(name='Team Beta', members=[carol.email])

        # Workouts
        Workout.objects.create(name='Pushups', description='20 pushups', points=5)
        Workout.objects.create(name='Running', description='Run 2km', points=10)
        Workout.objects.create(name='Jump Rope', description='Jump rope 5min', points=7)

        # Atividades (usando user_email)
        Activity.objects.create(user_email=alice.email, activity_type='Pushups', duration=10, date=date(2025, 4, 20), points=5)
        Activity.objects.create(user_email=bob.email, activity_type='Running', duration=20, date=date(2025, 4, 21), points=10)
        Activity.objects.create(user_email=carol.email, activity_type='Jump Rope', duration=5, date=date(2025, 4, 22), points=7)

        # Leaderboard (usando user_email)
        Leaderboard.objects.create(user_email=alice.email, total_points=5, rank=2)
        Leaderboard.objects.create(user_email=bob.email, total_points=10, rank=1)
        Leaderboard.objects.create(user_email=carol.email, total_points=7, rank=3)

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
