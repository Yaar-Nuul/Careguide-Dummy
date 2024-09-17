# myapp/management/commands/fetch_articles.py
from django.core.management.base import BaseCommand
from myapp.utils.web_scraping import save_articles_to_csv
class Command(BaseCommand):
    help = 'Fetches articles from predefined URLs and saves them to CSV'
    def handle(self, *args, **kwargs):
        save_articles_to_csv()
        self.stdout.write(self.style.SUCCESS('Articles successfully fetched and saved.'))