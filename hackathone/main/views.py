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
    detail_events_on = []
    detail_events_fresh = []
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
                    if i.groupId == "lotteon":
                        detail_events_on.append(str(i.title))
                    elif i.groupId == "lottefresh":
                        detail_events_fresh.append(str(i.title))


        # to use distinguish Boolean(having a todat's service data)
        length_on = len(detail_events_on)
        length_fresh = len(detail_events_fresh)
        message_on = ""
        message_fresh = ""
        for i in range(length_on):
            if i==0:
                message_on += str(detail_events_on[i])
            elif i>0:
                message_on += str(","+detail_events_on[i])
        for i in range(length_fresh):
            if i==0:
                message_fresh += str(detail_events_fresh[i])
            elif i>0:
                message_fresh += str(","+detail_events_fresh[i])

    return render(request, 'home.html', {'events': events, 'space': space, 'long_spcae': long_space, 'message_on':message_on, 'message_fresh':message_fresh, 'length_on':length_on, 'length_fresh':length_fresh})