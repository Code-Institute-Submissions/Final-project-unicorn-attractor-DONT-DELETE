from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Feature(models.Model):
    title = models.CharField(max_length=100, default="")
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    purchased = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FeatureComment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User)
    feature = models.ForeignKey(Feature)

    def __str__(self):
        return self.comment
