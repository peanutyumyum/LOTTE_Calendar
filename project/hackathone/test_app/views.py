from django.shortcuts import render
import calendar


# Create your views here.

def test(request):
    return render(request, 'test.html')