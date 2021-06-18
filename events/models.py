from django.db import models

# Create your models here.
class EventDetail(models.Model):
    name = models.CharField(max_length=50)
    event_image = models.ImageField(upload_to='events')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.CharField(max_length=20)
    description = models.TextField(max_length=700 ,null=True,blank=True)

    def __str__(self) :
        return self.name