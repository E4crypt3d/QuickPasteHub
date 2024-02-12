from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.query import QuerySet
from pygments import lexers
import uuid
# Create your models here.


class User(AbstractUser):
    pass


class PrivateManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(private=True)


class PublicManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(private=False)


class Snippet(models.Model):
    languages = [
        (f'{a[0]}', f'{a[0]}') for a in lexers.get_all_lexers()
    ]
    author = models.CharField(max_length=30)
    text = models.TextField()
    private = models.BooleanField(default=False)
    language = models.CharField(
        max_length=53, choices=languages)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=15, unique=True)
    editable = models.BooleanField(default=True)

    objects = models.Manager()
    privates = PrivateManager()
    public = PublicManager()

    def __str__(self):
        return self.author

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = str(uuid.uuid4())[:15]
        return super().save(*args, **kwargs)
