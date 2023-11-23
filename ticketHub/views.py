from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import EventDb
from .forms import EventForm
from django.contrib import messages



# Create your views here.
def home(request):
    all_events = EventDb.objects.all()
    for event in all_events:
        print(event.image,event.description, event.date, event.location)
    return render(request, 'homepage.html', {'all_events': all_events})


def events(request):
    return render(request, 'events.html')

@login_required()
def create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            all_events = EventDb.objects.all()
            messages.success(request, 'New Event created')
            print(form.errors)
            return render(request, 'create.html', {'all_events': all_events})
        else:
            messages.error(request, 'Form is not valid. Please check the entered data.')
            all_events = EventDb.objects.all()
            print(form.errors)
            return render(request,  'create.html', {'form': form, 'all_events': all_events})
    else:
        form = EventForm()  # Instantiate the form
        all_events = EventDb.objects.all()
        return render(request, 'create.html', {'form': form, 'all_events': all_events})



def delete(request, list_id):
    event = EventDb.objects.get(pk=list_id)
    event.delete()
    messages.success(request,('Event Deleted'))
    return redirect('create')

def testing(request):
    return render(request, 'testing.html')