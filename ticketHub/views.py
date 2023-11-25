from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import EventDb
from .forms import EventForm
from django.contrib import messages



# Create your views here.
def home(request):
    all_events = EventDb.objects.all()
    return render(request, 'homepage.html', {'all_events': all_events})


def events(request):
    all_events = EventDb.objects.all()
    return render(request, 'events.html',{'all_events': all_events})

@login_required()
def create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_event = form.save()
            print(f"New Event created: {new_event.Event_title}")
            messages.success(request, f'New Event "{new_event.Event_title}" created')
            return redirect('events')
        else:
            print("Form is not valid. Errors:", form.errors)
            messages.error(request, 'Form is not valid. Please check the entered data.')
    else:
        form = EventForm()

    all_events = EventDb.objects.all()
    return render(request, 'create.html', {'form': form, 'all_events': all_events})

def delete(request, event_id):
    try:
        event = EventDb.objects.get(pk=event_id)
        event.Event_title = event.Event_title
        event.delete()
        messages.success(request, f'Event "{event.Event_title}" deleted successfully')
    except EventDb.DoesNotExist:
        messages.error(request, 'Event not found')

    return redirect('events')



def testing(request):
    return render(request, 'testing.html')