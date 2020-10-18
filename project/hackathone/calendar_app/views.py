from django.shortcuts import render
from .models import CalendarEvent

# Create your views here.
def calendar(request):
    events = CalendarEvent.objects.all()
    space = "&nbsp;"
    long_space = space*10

    return render(request,'calendar.html',{'events':events, 'space' : space, 'long_spcae' : long_space})