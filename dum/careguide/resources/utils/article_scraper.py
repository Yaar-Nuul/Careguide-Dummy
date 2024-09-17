import requests
from bs4 import BeautifulSoup
def fetch_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.find('h1').get_text()
    content = soup.find('div', class_='article-content').get_text()
    return {
        'title': title,
        'content': content,
        'author': 'Author Name', 
        'published_date': None  
    }