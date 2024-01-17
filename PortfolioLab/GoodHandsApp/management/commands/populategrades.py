from django.core.management.base import BaseCommand
from ._private import create_students, create_subjects, create_grades


class Command(BaseCommand):
    help = 'Generuje losowe oceny dla każdego ucznia'

    def handle(self, *args, **options):
        create_grades()
        self.stdout.write(self.style.SUCCESS("Oceny wygenerowane!"))
