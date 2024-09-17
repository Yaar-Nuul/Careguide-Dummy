
from django.core.management.base import BaseCommand
from myapp.utils.web_scraping import save_texts_to_csv
class Command(BaseCommand):
    help = 'Extracts text from predefined URLs and saves it to CSV'
    def handle(self, *args, **kwargs):
        save_texts_to_csv()
        self.stdout.write(self.style.SUCCESS('Texts successfully extracted and saved.'))






