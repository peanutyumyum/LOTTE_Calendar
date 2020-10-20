from django.shortcuts import render
from .models import CalendarEvent
import datetime

# Create your views here.
def calendar(request):
    events = CalendarEvent.objects.all()
    space = "&nbsp;"
    long_space = space*10
    
    def detail_information_render(today_item):
        arr = []
        detail_events = CalendarEvent.objects.get(pk=today_item)
        for i in detail_events:
            arr.append(i)
        return arr
    


    for i in events:
        today = str(datetime.datetime.now())
        start_day = str(i.start)
        end_day = str(i.end)
        if today > start_day:
            if today < end_day:
                a = detail_information_render(i.id)
                

    return render(request,'calendar.html',{'events':events, 'space' : space, 'long_spcae' : long_space, 'detail_events' : a})

    # 2020-10-05 07:14:32+00:00