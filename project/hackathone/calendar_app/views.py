from django.shortcuts import render
from .models import CalendarEvent

# Create your views here.
def calendar(request):
    events = CalendarEvent.objects.all()
    space = "&nbsp;"
    long_space = space*10
    for i in events:
        a = str(i.start)[0:10]
    print(a)

    return render(request,'calendar.html',{'events':events, 'space' : space, 'long_spcae' : long_space})

    # 2020-10-05 07:14:32+00:00