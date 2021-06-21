from django.shortcuts import redirect, render
from .models import EventDetail
from .forms import CreateEvent


def home(request,*args,**kwargs):
    event_obj = EventDetail.objects.filter(approve=True)
    return render(request,'home.html',{"events":event_obj})
def profile(request,*args,**kwargs):
    events = EventDetail.objects.filter(approve=True)
    return render(request,'profile.html',{"events":events})

def create_event(request,*args,**kwargs):
    form = CreateEvent()
    events = EventDetail.objects.filter(approve=True)
    if request.method == 'POST':
        form = CreateEvent(request.POST or None,request.FILES or None)
        if form.is_valid():
            name = request.POST["name"]
            event_image = request.FILES["event_image"]
            date = request.POST["date"]
            start_time = request.POST["start_time"]
            end_time = request.POST["end_time"]
            venue = request.POST["venue"]
            description = request.POST["description"]
            print(222)
            event = EventDetail.objects.create(name=name,event_image=event_image,date=date,
            start_time=start_time,end_time=end_time,venue=venue,description=description,approve=False)
            event.save()
            return redirect("/user-profile")
    return render(request,'create_event.html',{"form":form})