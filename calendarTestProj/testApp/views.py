from django.shortcuts import render
from .models import CalendarEvent

# Create your views here.
def home(request):
    events = CalendarEvent.objects.all()
    print(events)
    return render(request,'home.html',{'events':events})