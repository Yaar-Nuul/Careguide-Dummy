
from rest_framework import serializers
from resources.models import Resources

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = ['id', 'title', 'content', 'author']  

    def __str__(self):
        return self.title
