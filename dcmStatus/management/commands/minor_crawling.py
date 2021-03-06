from django.core.management.base import BaseCommand, CommandError
from crawling import crawling


class Command(BaseCommand):
    help = 'Crawling minorGall rank'

    def handle(self, *args, **options):
        crawling.crawlingMinorgaall()

        self.stdout.write('MinorGall crawling finished')
