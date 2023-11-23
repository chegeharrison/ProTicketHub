from django import forms
from .models import EventDb

class EventForm(forms.ModelForm):
    class Meta:
        model = EventDb
        fields =['image', 'description','date','location']

    def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)

            placeholders = {
                'image': 'Provide your Poster Here',
                'description': 'Provide your Description Here',
                'date': 'Provide the Date Here',
                'location': 'Provide the Location Here',
            }
            for field_name, placeholder_text in placeholders.items():
                self.fields[field_name].widget.attrs['placeholder'] = placeholder_text