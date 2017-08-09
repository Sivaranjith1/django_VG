from django.db import models

# Create your models here.

class Article(models.Model):
    image_title = models.CharField(max_length=100)
    image_text = models.CharField(max_length=70, blank=True)
    title = models.CharField(max_length=70)
    #date = models.DateTimeField()
    ingress = models.TextField(blank=True)
    hoveddel = models.TextField(blank=True)
    #image_mellom = models.TextField(blank = True)
    #image_mellomtext = models.TextField(blank = True)

    def __str__(self):
        return self.title