from django.shortcuts import render, redirect
from shop.models import Product
from main.models import CalendarEvent
from datetime import datetime, timedelta

def order_detail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'order/order.html',{'product':product}) 

def order(request):
    if request.user.is_authenticated:
           user = request.user
    if request.method == "POST":
        if request.POST['product_category'] == "lotteon":
            num = int(request.POST['month'])*30
            date_req = request.POST['startdate']
            date_array = date_req.split('-')
            start_time = datetime(int(date_array[0]), int(date_array[1]), int(date_array[2]), 0, 0, 0)
            for i in range(2):
                if i > 0 :
                    date_real = start_time + timedelta(days=num)
                else :
                    date_real = start_time
                event_obj = CalendarEvent()
                event_obj.author= user
                event_obj.title = request.POST['product_name']
                event_obj.start = date_real
                event_obj.end = date_real
                event_obj.groupId = request.POST['product_category']
                event_obj.save()

        if request.POST['product_category'] == "lottefresh":
            month = int(request.POST['month'])
            week = int(request.POST['week'])
            date_req = request.POST['startdate']
            date_array = date_req.split('-')
            start_time = datetime(int(date_array[0]), int(date_array[1]), int(date_array[2]), 0, 0, 0)
            for i in range(month//week):
                if i > 0 :
                    date_real = start_time + timedelta(days=i*week*7)
                else :
                    date_real = start_time
                event_obj = CalendarEvent()
                event_obj.author= user
                event_obj.title = request.POST['product_name']
                event_obj.start = date_real
                event_obj.end = date_real
                event_obj.groupId = request.POST['product_category']
                event_obj.save()
        return redirect('main:home') 
    else:
        pass
    return render(request, 'order.html')