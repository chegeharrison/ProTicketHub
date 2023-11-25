from django import forms
from .models import EventDb

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type ='time'

class EventForm(forms.ModelForm):
    class Meta:
        model = EventDb
        fields =['Poster', 'Event_title','Date','Time','Location']
        widgets = {
            'Date': DateInput(),
            'Time': TimeInput

        }

    def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)

            placeholders = {
                'Poster': 'Provide your Poster Here',
                'Event_title': 'Provide your Event_title',
                'Time':'Provide time when event start',
                'Date': 'Provide the Date Here',
                'Location': 'Provide the Location Here',
            }
            for field_name, placeholder_text in placeholders.items():
                self.fields[field_name].widget.attrs['placeholder'] = placeholder_text