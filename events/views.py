from django.shortcuts import redirect, render
from .models import EventDetail
from .forms import CreateEvent

# Create your views here.
def home(request,*args,**kwargs):
    event_obj = EventDetail.objects.all()
    return render(request,'home.html',{"events":event_obj})
def profile(request,*args,**kwargs):
    print("profile vannu")
    events = EventDetail.objects.all()
    return render(request,'profile.html',{"events":events})

def create_event(request,*args,**kwargs):
    events = EventDetail.objects.all()
    print("crate_evnet vannu")
    form = CreateEvent(request.POST or None )
    if request.method =="POST":
        name = request.POST["name"]
        event_image = request.POST["event_image"]
        date = request.POST["date"]
        start_time = request.POST["start_time"]
        end_time = request.POST["end_time"]
        venue = request.POST["venue"]
        description = request.POST["description"]
        event = EventDetail.objects.create(name=name,event_image=event_image,date=date,start_time=start_time,end_time=end_time,venue=venue,description=description)
        event.save()
        return render(request,'profile.html',{"events":events})
    return render(request,'create_event.html',{"form":form})