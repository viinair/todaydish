from django.core.management.base import BaseCommand
from  todaydishApp.models import Dish

class Command(BaseCommand):
    help = 'Seed the database with some dishes'

    def handle(self, *args, **options):
        dishes = [
            {'name': 'Dosa'},
            {'name': 'Idli'},
            {'name': 'Samosa'},
            {'name': 'Vada'},
            {'name': 'Uttapam'},
            {'name': 'Aloo Tikki'},
            {'name': 'Puri'},
            {'name': 'Biryani'},
            {'name': 'Butter Chicken'},
            {'name': 'Palak Paneer'},
        ]

        for dish in dishes:
            Dish.objects.create(**dish)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with dishes.'))
