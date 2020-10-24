from django.shortcuts import render

# Create your views here.

def home(request):
    context = {

    }
    return render(request, 'home.html', context)


def first(request):
    context = {

    }
    return render(request, 'first.html', context)