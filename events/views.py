import events
from django.shortcuts import redirect, render
from .models import EventDetail,EventRegister
from .forms import CreateEvent , Registration


def home(request,*args,**kwargs):
    event_obj = EventDetail.objects.filter(approve=True)
    return render(request,'home.html',{"events":event_obj})
def profile(request,*args,**kwargs):
    user = request.user
    my_events = EventRegister.objects.filter(user = user)
    events = EventDetail.objects.filter(approve=True)
    return render(request,'profile.html',{"events":events,"my_events":my_events})

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
            event = EventDetail.objects.create(name=name,event_image=event_image,date=date,
            start_time=start_time,end_time=end_time,venue=venue,description=description,approve=False)
            event.save()
            return redirect("/user-profile")
    return render(request,'create_event.html',{"form":form})


def registration(request,*args,**kwargs):
    form = Registration(request.POST or None)
    instance = EventRegister
    if request.method=="POST":
        if form.is_valid():
            event= request.POST["events"]
            user = request.user
            current = EventDetail.objects.filter(name=event)
            current_event = current.first()
            phone = request.POST["phone"]
            evnt_register=instance.objects.create(user = user,event=current_event,mobile=phone)
            evnt_register.save()
            return redirect("/user-profile")
    return render(request,'registration.html',{"form":form})


def participants_list(request, pk,*args,**kwargs):
    event = EventDetail.objects.get(id = pk)
    name = EventRegister.objects.filter(event = event)
    return render(request,'participants_list.html',{"list":name})