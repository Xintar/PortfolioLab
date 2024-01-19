from django.core.management.base import BaseCommand
from ._private import create_institution


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_institution()
        self.stdout.write(self.style.SUCCESS("Succesfully add institution."))
