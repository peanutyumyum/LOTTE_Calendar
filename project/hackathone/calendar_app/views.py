from django.shortcuts import render
from .models import CalendarEvent

# Create your views here.
def calendar(request):
    events = CalendarEvent.objects.all()
    print(events)
    return render(request,'calendar.html',{'events':events})