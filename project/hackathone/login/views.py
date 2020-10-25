from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Member
User = get_user_model()

# Create your views here.


def signup(request):
    if request.method == 'POST':
        # 아이디 중복 체크
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            # 회원가입시 자동으로 로그인되지 않도록.
            #auth.login(request, user)
            return redirect('main:home')
        else:
            return redirect('signup:home')
    return render(request, 'signup.html')


def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main:home')
        else:
            messages.info(request, "회원가입이 필요합니다.")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    # messages.info(request, "로그아웃이 완료되었습니다.")
    auth.logout(request)
    return redirect('main:home')
