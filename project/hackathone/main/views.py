from django.shortcuts import render
from .models import CalendarEvent
import datetime

# Create your views here.


def home(request):
    print("실행")
    events = CalendarEvent.objects.all()
    space = "&nbsp;"
    long_space = space*10

    def detail_information_render(today_item):

        detail_event = CalendarEvent.objects.get(pk=today_item)
        return detail_event

    detail_events = []

    for i in events:
        today_date = str(datetime.datetime.now())[0:10]
        today_str = today_date.replace("-", "")
        today = int(today_str)

        start_day_date = str(i.start)[0:10]
        start_day_str = start_day_date.replace("-", "")
        start_day = int(start_day_str)

        end_day_date = str(i.end)[0:10]
        end_day_str = end_day_date.replace("-", "")
        end_day = int(end_day_str)

        if today >= start_day:
            if today <= end_day:
                detail_events.append(detail_information_render(i.id))

    print("확인")
    print(events)

    return render(request, 'home.html', {'events': events, 'space': space, 'long_spcae': long_space, 'detail_events': detail_events})
  
def first(request):
  context = {

  }
  return render(request, 'first.html', context)