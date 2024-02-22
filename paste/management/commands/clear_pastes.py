from django.core.management.base import BaseCommand, CommandError
from paste.models import Snippet
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = "Deletes the expired or month old pastes"

    def handle(self, *args, **options):
        try:
            # Calculate the datetime 30 days ago
            time = timezone.now() - timedelta(days=30)

            # Filter Snippet objects modified before 30 days ago
            pastes = Snippet.objects.filter(modified_at__lt=time)
            # Check if any pastes were found
            if pastes.exists() and pastes.count() > 10:
                # Delete the pastes
                pastes.delete()
                self.stdout.write(
                    self.style.SUCCESS('Successfully cleared old pastes'))
            else:
                self.stdout.write(
                    self.style.SUCCESS('No old pastes found'))
        except Exception as e:
            raise CommandError(f'Something went wrong: {e}')
