from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .choices import Option
from .managers import PostObjects


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    status = models.CharField(
        max_length=11, choices=Option.choices, default=Option.PUBLISHED
    )
    objects = models.Manager()  # default manager
    articleobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.title
