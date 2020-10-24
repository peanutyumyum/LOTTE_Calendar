from django.shortcuts import render

def mypage(request):
    context = {
    }
    return render(request, 'mypage.html', context)

def delivery(request):
    context = {
    }
    return render(request, 'delivery.html', context)  
def notice(request):
    context = {
    }
    return render(request, 'notice.html', context)  
def event(request):
    context = {
    }
    return render(request, 'event.html', context) 
def basket(request):
    context = {
    }
    return render(request, 'basket.html', context)  