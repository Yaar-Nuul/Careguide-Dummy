
from django.db import models

class Resources(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


