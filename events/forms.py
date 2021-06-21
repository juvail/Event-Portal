from django import forms

class CreateEvent(forms.Form):
    name = forms.CharField(max_length=50)
    event_image = forms.ImageField()
    date = forms.DateField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    venue = forms.CharField(max_length=20)
    description = forms.CharField(max_length=700)

    def clean_name(self):
        name = self.cleaned_data["name"]
        return name
    def clean_event_image(self):
        event_image = self.cleaned_data["event_image"]
        return event_image
    def clean_date(self):
        date = self.cleaned_data["date"]
        return date
    def clean_start_time(self):
        start_time=self.cleaned_data["start_time"]
        return start_time
    def clean_end_time(self):
        end_time = self.cleaned_data["end_time"]
        return end_time
    def clean_venue(self):
        venue = self.cleaned_data["venue"]
        return venue
    def clean_description(self):
        description = self.cleaned_data["description"]
        return description
