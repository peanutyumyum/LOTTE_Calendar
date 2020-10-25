# import user data

from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User # user data


# custom import

from django.shortcuts import render
from .models import CalendarEvent


# usage for time filter function

import datetime


# Create your views here.


def home(request):
    events = CalendarEvent.objects.all()
    space = "&nbsp;"
    long_space = space*10
    def detail_information_render(today_item):

        detail_event = CalendarEvent.objects.get(pk=today_item)
        return detail_event

    detail_events = []
    for i in events:
            user = request.user
            if i.author == request.user:
                today_date = str(datetime.datetime.now())[0:9]
                today_str = today_date.replace("-", "")
                today = int(today_str)

                start_day_date = str(i.start)[0:9]
                start_day_str = start_day_date.replace("-", "")
                start_day = int(start_day_str)

                end_day_date = str(i.end)[0:9]
                end_day_str = end_day_date.replace("-", "")
                end_day = int(end_day_str)

                if today >= start_day and today<=end_day:
                    detail_events.append(i.title)
                
            length = len(detail_events)
    return render(request, 'home.html', {'events': events, 'space': space, 'long_spcae': long_space, 'detail_events': detail_events, 'length':length})
  
def first(request):
    
    context = {

    }
    return render(request, 'first.html', context)

