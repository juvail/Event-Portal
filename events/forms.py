from django import forms

class CreateEvent(forms.Form):
    name = forms.CharField(max_length=50)
    event_image = forms.ImageField()
    date = forms.DateField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    venue = forms.CharField(max_length=20)
    description = forms.CharField(max_length=700)

