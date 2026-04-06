from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from djongo import models

# Define models for teams, activities, leaderboard, and workouts
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create_user(username='tony', email='tony@marvel.com', password='ironman')
        bruce = User.objects.create_user(username='bruce', email='bruce@marvel.com', password='hulk')
        clark = User.objects.create_user(username='clark', email='clark@dc.com', password='superman')
        diana = User.objects.create_user(username='diana', email='diana@dc.com', password='wonderwoman')

        # Create activities
        Activity.objects.create(user=tony, type='Running', duration=30)
        Activity.objects.create(user=bruce, type='Cycling', duration=45)
        Activity.objects.create(user=clark, type='Swimming', duration=60)
        Activity.objects.create(user=diana, type='Yoga', duration=40)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility')

        # Create leaderboard
        Leaderboard.objects.create(user=tony, points=100)
        Leaderboard.objects.create(user=bruce, points=80)
        Leaderboard.objects.create(user=clark, points=120)
        Leaderboard.objects.create(user=diana, points=110)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
