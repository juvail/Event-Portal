from django.shortcuts import render
from .models import EventDetail



# Create your views here.
def home(request):
    event_obj = EventDetail.objects.all()
    return render(request,'home.html',{"events":event_obj})