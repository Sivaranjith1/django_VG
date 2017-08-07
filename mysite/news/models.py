from django.db import models

# Create your models here.

class article(models.Model):
    image_title = models.CharField(max_length=100)
    image_text = models.CharField(max_length=70)
    title = models.CharField(max_length=70)
    ingress = models.TextField()
    hoveddel = models.TextField()
    image_mellom = models.TextField(blank = True)
    image_mellomtext = models.TextField(blank = True)
    
    
