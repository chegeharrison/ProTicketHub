from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm,TicketForm,PaymentForm,EventApprovalRequestForm
from django.contrib import messages
from django_daraja.mpesa.core import MpesaClient
from django_daraja.mpesa.exceptions import MpesaInvalidParameterException
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EventDb, Ticket, Payment

# Create your views here.
def home(request):
    # Only fetch events that are approved
    all_events = EventDb.objects.filter(approved=True)
    return render(request, 'homepage.html', {'all_events': all_events})
@login_required()
def events(request):
    all_events = EventDb.objects.all()
    for event in all_events:
        print('poster:', event.Poster)
    return render(request, 'events.html',{'all_events': all_events})

@login_required()
def create(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES or None)
        if event_form.is_valid():
            new_event = event_form.save()
            messages.success(request, f'New Event "{new_event.Event_title}" created')
            return redirect('events')
        else:
            messages.error(request, 'Event Form is not valid. Please check the entered data.')
    else:
        event_form = EventForm()

    all_events = EventDb.objects.all()
    return render(request, 'create.html', {'event_form': event_form, 'all_events': all_events})

def delete(request, event_id):
    try:
        event = EventDb.objects.get(pk=event_id)

        # Check if the event is approved
        if event.approved:
            messages.error(request, f'Cannot delete approved event "{event.Event_title}"')
        else:
            event_title = event.Event_title
            event.delete()
            messages.success(request, f'Event "{event_title}" deleted successfully')

    except EventDb.DoesNotExist:
        messages.error(request, 'Event not found')

    return redirect('events')



def ticket(request, event_id):
    event = EventDb.objects.get(pk=event_id)
    tickets = Ticket.objects.filter(event=event)

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.event = event
            ticket.save()
            calculated_amount = ticket.price
            payment_form = PaymentForm(initial={'calculated_amount': calculated_amount})
            messages.success(request, 'Ticket created successfully')
            return render(request, 'payment.html', {'event': event, 'form': payment_form})
        else:
            messages.error(request, 'Ticket Form is not valid. Please check the entered data.')
    else:
        form = TicketForm()
    ticket_prices = {}
    for choice in form.fields['ticket_type'].choices:
        tickets_matching_type = event.ticket_set.filter(ticket_type=choice[0])
        if tickets_matching_type.exists():
            ticket_prices[choice[0]] = tickets_matching_type.first().price
        else:
            ticket_prices[choice[0]] = 0  # Set a default price

    return render(request, 'ticket.html',
                  {'event': event, 'form': form, 'tickets': tickets, 'ticket_prices': ticket_prices})

@csrf_exempt
def payment(request, event_id):
    event = EventDb.objects.get(pk=event_id)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            calculated_amount = form.cleaned_data['calculated_amount']
            payment = Payment(
                calculated_amount=calculated_amount,
                phone_number=phone_number,
            )
            payment.save()
            if request.user.is_authenticated:
                name = request.user.username
            else:
              name = "Guest User"
            amount = int(calculated_amount)
            account_reference = 'reference'
            transaction_desc = 'Description'
            callback_url = 'https://api.darajambili.com/express-payment'
            customer = MpesaClient()
            try:
                response = customer.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
                if response.status_code == 200:
                    return HttpResponse(f"Payment successful for {name}.")
                else:
                    return HttpResponse(f"Payment failed for {name}. Please try again.")
            except MpesaInvalidParameterException as e:
                return HttpResponse(f"Payment failed. {e}")
        else:
            return HttpResponse("Invalid form data. Please check your input.")
    else:
        calculated_amount = request.GET.get('calculated_amount')

        form = PaymentForm(initial={'calculated_amount': calculated_amount, 'ticket': ticket})

    return render(request, 'payment.html', {'event': event, 'form': form})


def request_approval(request, event_id):
    event = EventDb.objects.get(pk=event_id)

    if request.method == 'POST':
        form = EventApprovalRequestForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['submit_request']:
                event.request_approval()
                messages.success(request, f'Request for approval sent for event "{event.Event_title}"')
                # Redirect to the same page to stay on event.html
                return redirect('events', event_id=event.id)

    else:
        form = EventApprovalRequestForm()

    return render(request, 'approval.html', {'event': event, 'approval_request_form': form})
