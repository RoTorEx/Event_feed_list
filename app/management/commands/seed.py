import random as r
from os import listdir

from django.contrib.auth.models import User as DefaultUser
from django.core.management.base import BaseCommand
from django_seed import Seed

from app.models import Achievement, Advertising, Post, User


USER = r.randint(2, 3)
POST = r.randint(4, 10)
ACHIEVEMENT = r.randint(2, 6)
ADVERTISING = r.randint(1, 3)


class Command(BaseCommand):
    help = """Expanding the functionality of the basic app commands."""

    def handle(self, *args, **options):
        """Fill database."""

        # Create superusers
        if not DefaultUser.objects.filter(username__in=("root", "admin")):
            DefaultUser.objects.create_superuser("root", "root@example.com", "1234")
            DefaultUser.objects.create_superuser("admin", "admin@example.com", "admin")

        seeder = Seed.seeder()

        seeder.add_entity(User, USER)
        seeder.add_entity(Post, POST)
        seeder.add_entity(Achievement, ACHIEVEMENT)
        seeder.add_entity(Advertising, ADVERTISING)

        seeder.execute()

        # Path to images
        achievement_image = listdir("./media/achievement_image")
        advertising_image = listdir("./media/advertising_image")

        # Set random images to Achievements and Advertisements
        # !Warning! N+1 requests in list comprehations :)
        [
            Achievement.objects.filter(pk=i + 1).update(image=f"achievement_image/{r.choice(achievement_image)}")
            for i in range(len(Achievement.objects.all()))
        ]
        [
            Advertising.objects.filter(pk=i + 1).update(image=f"advertising_image/{r.choice(advertising_image)}")
            for i in range(len(Advertising.objects.all()))
        ]
