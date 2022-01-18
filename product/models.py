from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    # title
    title = models.CharField(max_length=200, default="")
    # publication date
    pub_date = models.DateTimeField(default=timezone.datetime.now())
    # body
    body = models.TextField(max_length=1000, default="")
    url = models.TextField(max_length=1000, default="")
    # image
    image = models.ImageField(upload_to='images/', default="")
    icon = models.ImageField(upload_to='images/', default="")
    votes_total = models.IntegerField(default=1)
    voters = set()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    
    def __str__(self) -> str:  # On admin page, object name will be showed as title
        return self.title

    def summary(self):
        if len(self.body) > 200:
            return self.body[:100]+"..."
        return self.body

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
