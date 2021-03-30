from django.core.management.base import BaseCommand, CommandError
from question.models import Question
from crawling import crawling


class Command(BaseCommand):
    help = 'Crawling minorGall Rank'

    def handle(self, *args, **options):
        crawling.crawlingMinorgaall()

        self.stdout.write('MinorGall crawling finished')
