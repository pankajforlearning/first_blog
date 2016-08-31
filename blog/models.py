from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
   author = models.CharField(max_length=150)
   title = models.CharField(max_length=200)
   text = models.TextField()
   create_date = models.DateTimeField(default=timezone.now)
   published_date = models.DateTimeField(blank=True, null=True)
  
   def publish(publishing_date):
       publishing_date.published.date = timezone.now()
       publishing_date.save()

   
