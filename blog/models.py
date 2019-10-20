from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    summary = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    def new_summary(self):
        return self.summary[:200] + ' ...Click to read more'

    def new_date(self):
        return self.date.strftime('%b %e, %Y')


