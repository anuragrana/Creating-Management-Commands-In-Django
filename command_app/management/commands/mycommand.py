from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Command to do....something...lets print on screen.'

    def add_argument(self, parser):
        pass
        
    def handle(self, *args, **options):
        try:
            print("I am here")
        except Exception as e:
            raise CommandError(repr(e))


