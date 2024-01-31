from django.core.management.base import BaseCommand
from ._private import create_donation


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_donation()
        self.stdout.write(self.style.SUCCESS("Succesfully add donations."))
