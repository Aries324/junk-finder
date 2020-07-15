from django.core.management.base import BaseCommand

from junkapp.models import ItemsPost

class Command(BaseCommand):
    help = 'Select the category of item that you want to post'

    def handle(self, *args, **options):
        for item in ItemsPost.ITEM_CHOICES:
            ItemsPost.objects.create(
                items=item[0]
            )
            self.stdout.write(self.style.SUCCESS('Your item "%s" has been added!' % item[1]))