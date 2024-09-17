 
from django.urls import path
from api.views import ResourcesListCreateView, ScrapeResourcesView

urlpatterns = [
    path('resources/', ResourcesListCreateView.as_view(), name='resources-list-create'),
    path('article_scraper/', ScrapeResourcesView.as_view(), name='article_scrape'),
]


