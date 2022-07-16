from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    image = models.ImageField(upload_to='posts')
    content = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateField()
    author_name = models.CharField(max_length=255)
    author_image = models.ImageField(upload_to='author')
    author_comment = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='comment photo')
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
