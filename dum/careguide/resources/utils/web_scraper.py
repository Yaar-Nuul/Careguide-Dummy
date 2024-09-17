import os
import django
import requests
from bs4 import BeautifulSoup
import sys

sys.path.append('/home/student/Documents/dum/careguide')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'careguide.settings')  
django.setup()

from resources.models import Resources  

urls_scrape = [
    'https://magazine.medlineplus.gov/article/getting-help-for-mental-health/',
    'https://www.medicalnewstoday.com/articles/160774#micronutrients',
    'https://www.healthline.com/nutrition/10-reasons-why-good-sleep-is-important#2.-Can-improve-concentration-and-productivity',
    'https://www.betterhealth.vic.gov.au/health/healthyliving/postnatal-exercise',
]

def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('title').get_text(strip=True)

    author = ''
    author_meta = soup.find('meta', {'name': 'author'})
    if author_meta:
        author = author_meta.get('content', '').strip()
    else:
        author_tag = soup.find('span', class_='author') or soup.find('a', class_='author')
        if author_tag:
            author = author_tag.get_text(strip=True)

    pub_date = ''
    date_meta = soup.find('meta', {'property': 'article:published_time'}) or \
                soup.find('meta', {'name': 'date'}) or \
                soup.find('meta', {'property': 'og:pubdate'})
    if date_meta:
        pub_date = date_meta.get('content', '').strip()
    else:
        date_tag = soup.find('time')
        if date_tag:
            pub_date = date_tag.get_text(strip=True)

    body_content = soup.find('div', class_='main-content') or soup.find('div', id='content')
    text = ''
    if body_content:
        for unwanted in body_content.find_all(['footer', 'nav', 'aside']):
            unwanted.decompose()
        text = ' '.join([p.get_text(strip=True) for p in body_content.find_all('p')])

    return {
        'Title': title,
        'Author': author,
        'Publication Date': pub_date,
        'Content': text
    }


for url in urls_scrape:
    try:
        article_data = scrape_article(url)
        pub_date = pd.to_datetime(article_data['Publication Date'], errors='coerce') if article_data['Publication Date'] else None

        Resources.objects.update_or_create(
            title=article_data['Title'],
            defaults={
                'author': article_data['Author'],
                'publication_date': pub_date,
                'content': article_data['Content']
            }
        )
        print(f'Successfully saved: {url}')
    except Exception as e:
        print(f'Failed to save {url}: {e}')

urls_extract = [
    'https://www.mentalhealth.org.uk/explore-mental-health/publications/our-best-mental-health-tips',
    'https://www.whattoexpect.com/first-year/postpartum/postpartum-diet-nutrition-questions-answered/',
    'https://nichq.org/insight/better-sleep-breastfeeding-mothers-safer-sleep-babies',
    'https://www.betterhealth.vic.gov.au/health/healthyliving/postnatal-exercise',
]

def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('title').get_text(strip=True)

    for tag in soup(['script', 'style', 'footer', 'nav', 'header']):
        tag.decompose()

    text = soup.get_text(separator=' ', strip=True)

    return {
        'URL': url,
        'Title': title,
        'Text': text
    }


for url in urls_extract:
    try:
        text_data = extract_text(url)
        Resources.objects.update_or_create(
            title=text_data['Title'],
            defaults={
                'content': text_data['Text'],
                'author': '',
                'publication_date': None
            }
        )
        print(f'Successfully saved: {url}')
    except Exception as e:
        print(f'Failed to save {url}: {e}')
