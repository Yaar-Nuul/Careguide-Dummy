from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from resources.models import Resources
from .serializers import ResourcesSerializer
from resources.utils import article_scraper


class ResourcesListCreateView(generics.ListCreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer



class ScrapeResourcesView(APIView):
    def post(self, request):
        url = request.data.get('url')
        if not url:
            return Response({"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            title, content, images, videos = scrape_article(url)
            resources = Resources.objects.create(
                title=title,
                content=content,
                images=images,
                videos=videos,
            )
            serializer = ResourcesSerializer(resources)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class ResourcesListView(APIView):
    def get(self, request):
        resources= Resources.objects.all()
        serializer = ResourcesSerializer(resources, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)