from django.core.management.base import BaseCommand
from rooms.models import Rule


class Command(BaseCommand):

    help = "This command create rule data"

    def handle(self, *args, **options):
        rules = [
            "State Check In and Out time",
            "No Pets",
            "No Parties or Event",
            "Don't smoke",
        ]
        for r in rules:
            Rule.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS(f"{len(rules)} house rule created!"))
