import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users.models import User


class Command(BaseCommand):

    help = "This command create rooms data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many room data do you want"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        users = User.objects.all()
        room_types = room_models.RoomType.objects.all()
        print(room_types, users)
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(0, 500),
                "guests": lambda x: random.randint(0, 20),
                "beds": lambda x: random.randint(0, 5),
                "bedrooms": lambda x: random.randint(0, 5),
                "baths": lambda x: random.randint(0, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facility = room_models.Facility.objects.all()
        rules = room_models.Rule.objects.all()
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    photo_file=f"room_photos/{random.randint(1, 31)}.webp",
                    room=room,
                )
            for a in amenities:
                rand_number = random.randint(0, 15)
                if rand_number % 2 == 0:
                    room.amenities.add(a)
            for a in facility:
                rand_number = random.randint(0, 15)
                if rand_number % 2 == 0:
                    room.facility.add(a)
            for a in rules:
                rand_number = random.randint(0, 15)
                if rand_number % 2 == 0:
                    room.rule.add(a)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
