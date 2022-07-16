from django.db import models
from articles.models import Tag


class Team(models.Model):
    author_name = models.CharField(max_length=255)
    author_image = models.ImageField(upload_to='author')
    author_comment = models.TextField()
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.author_name
