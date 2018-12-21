from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Bug(models.Model):
    app_choices = [
        ("bug", "Bug"),
        ("feature", "Feature")
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class BugComment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User)
    bug = models.ForeignKey(Bug)

    def __str__(self):
        return self.comment