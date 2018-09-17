from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateField(auto_now_add=True)
    summary = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

