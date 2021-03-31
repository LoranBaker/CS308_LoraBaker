from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100, default='title')
    authors = models.CharField(max_length=100, default='author')
    publisher = models.CharField(max_length=100,default='publisher')
    publication_date = models.DateTimeField(auto_now_add=True)
    number_of_pages = models.IntegerField(default=0)