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

# introducing page when you first open
def first(request):
    
    context = {

    }
    return render(request, 'first.html', context)


# main home page
def home(request):
    # define calendar QuerySet
    events = CalendarEvent.objects.all()


    # useful items at html content
    space = "&nbsp;"
    long_space = space*10


    # filtering today's events
    detail_events = []
    for i in events:
        if i.author == request.user:
            # todat settings
            today_date = str(datetime.datetime.now())[0:10]
            today_str = today_date.replace("-", "")
            today = int(today_str)

            # start day settings
            start_day_date = str(i.start)[0:10]
            start_day_str = start_day_date.replace("-", "")
            start_day = int(start_day_str)

            # end day settings
            end_day_date = str(i.end)[0:10]
            end_day_str = end_day_date.replace("-", "")
            end_day = int(end_day_str)

            # filtering
            if today >= start_day:
                if today <= end_day:
                    detail_events.append(str(i.title))


        # to use distinguish Boolean(having a todat's service data)
        length = len(detail_events)
        message = ""
        for i in range(length):
            if i==0:
                message += str(detail_events[i])
            elif i>0:
                message += str(","+detail_events[i])


    return render(request, 'home.html', {'events': events, 'space': space, 'long_spcae': long_space, 'detail_events': detail_events, 'message':message})