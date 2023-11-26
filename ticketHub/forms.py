from django import forms
from .models import EventDb,Ticket,Payment
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventForm(forms.ModelForm):
    class Meta:
        model = EventDb
        fields = ['Poster', 'Event_title', 'Date', 'Time', 'Location', 'advanced_price', 'gate_price', 'vip_price', 'vvip_price']
        widgets = {
            'Date': DateInput(),
            'Time': TimeInput(),
        }

    def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)

            placeholders = {
                'Poster': 'Provide your Poster Here',
                'Event_title': 'Provide your Event_title',
                'Date': 'Provide the Date Here',
                'Time': 'Provide the Time Here',
                'Location': 'Provide the Location Here',
                'advanced_price': 'Enter Advanced Ticket Price',
                'gate_price': 'Enter Gate Ticket Price',
                'vip_price': 'Enter VIP Ticket Price',
                'vvip_price': 'Enter VVIP Ticket Price',

            }
            for field_name, placeholder_text in placeholders.items():
                self.fields[field_name].widget.attrs['placeholder'] = placeholder_text


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_type', 'quantity']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['phone_number', 'calculated_amount', 'ticket']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['calculated_amount'].widget.attrs['readonly'] = True

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        # Ensure that the phone number contains only numeric characters
        if not phone_number.isdigit():
            raise ValidationError("Phone number must contain only numeric characters.")

        return phone_number