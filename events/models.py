from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

User = get_user_model()

# Create your models here.
class EventDetail(models.Model):
    name = models.CharField(max_length=50)
    event_image = models.ImageField(upload_to='events')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.CharField(max_length=20)
    description = models.TextField(max_length=700 ,null=True,blank=True)
    approve = models.BooleanField(default=False)

    def __str__(self) :
        return str(self.name) if self.name else ""

class EventRegister(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True , blank=True)
    event = models.ForeignKey(EventDetail,on_delete=models.CASCADE, null=True)
    mobile = models.CharField(max_length=13)
    

    def __str__(self):
        return str(self.user) if self.user else ""