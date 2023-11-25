from django.db import models
# from django_google_maps import fields as map_fields

# Create your models here.
class EventDb(models.Model):
    Poster = models.ImageField(upload_to='static/media', blank=True, null=True)
    Event_title = models.CharField(max_length=30, null=True)
    Date = models.DateField()
    Time = models.TimeField(null=True)
    Location = models.CharField(max_length=100)
    def __str__(self):
        return "%s %s %s %s %s"%(self.Poster, self.Event_title, self.Date, self.Time, self.Location)