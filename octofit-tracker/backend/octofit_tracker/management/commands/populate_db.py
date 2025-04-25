from django.core.management.base import BaseCommand
from ...models import OctofitUser, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Popula o banco octofit_db com dados de teste para users, teams, activities, leaderboard e workouts.'

    def handle(self, *args, **kwargs):
        # Limpa dados antigos
        OctofitUser.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Usuários
        alice = OctofitUser.objects.create(email='alice@octofit.com', name='Alice', password='alicepass')
        bob = OctofitUser.objects.create(email='bob@octofit.com', name='Bob', password='bobpass')
        carol = OctofitUser.objects.create(email='carol@octofit.com', name='Carol', password='carolpass')
        dave = OctofitUser.objects.create(email='dave@octofit.com', name='Dave', password='davepass')

        # Times (diversos casos)
        team1 = Team.objects.create(name='Team Alpha', members=[alice.email, bob.email])
        team2 = Team.objects.create(name='Team Beta', members=[carol.email])
        team3 = Team.objects.create(name='Team Gamma', members=[alice.email, carol.email, dave.email])
        team4 = Team.objects.create(name='Team Solo', members=[])

        # Workouts
        Workout.objects.create(name='Pushups', description='20 pushups', points=5)
        Workout.objects.create(name='Running', description='Run 2km', points=10)
        Workout.objects.create(name='Jump Rope', description='Jump rope 5min', points=7)
        Workout.objects.create(name='Plank', description='Hold plank for 1min', points=4)

        # Atividades (diversidade de usuários e datas)
        Activity.objects.create(user_email=alice.email, activity_type='Pushups', duration=10, date=date(2025, 4, 20), points=5)
        Activity.objects.create(user_email=bob.email, activity_type='Running', duration=20, date=date(2025, 4, 21), points=10)
        Activity.objects.create(user_email=carol.email, activity_type='Jump Rope', duration=5, date=date(2025, 4, 22), points=7)
        Activity.objects.create(user_email=dave.email, activity_type='Plank', duration=2, date=date(2025, 4, 23), points=4)
        Activity.objects.create(user_email=alice.email, activity_type='Running', duration=15, date=date(2025, 4, 24), points=10)

        # Leaderboard (diversidade de pontuação)
        Leaderboard.objects.create(user_email=alice.email, total_points=15, rank=1)
        Leaderboard.objects.create(user_email=bob.email, total_points=10, rank=2)
        Leaderboard.objects.create(user_email=carol.email, total_points=7, rank=3)
        Leaderboard.objects.create(user_email=dave.email, total_points=4, rank=4)

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste diversos!'))
