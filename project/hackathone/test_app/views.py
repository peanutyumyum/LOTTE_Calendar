from django.shortcuts import render
import calendar


# Create your views here.

def test(request):
    return render(request, 'test.html')

htmlCalendar = calendar.HTMLCalendar(calendar.SUNDAY)
s = htmlCalendar.formatmonth(2020,10)
print(s)
date =[]
for i in date:
    mark = "<script src='%s'></script>" % i
