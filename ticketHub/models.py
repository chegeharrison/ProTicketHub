from django.db import models

# Create your models here.
class EventDb(models.Model):
    image = models.ImageField(upload_to='static/media', blank=True, null=True)
    description = models.TextField(max_length=30)
    date = models.DateField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return "%s %s %s %s"%(self.image, self.description, self.date, self.location)
