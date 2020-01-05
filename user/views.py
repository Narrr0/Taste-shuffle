from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User

def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            user=User.objects.create_user(username=request.POSt['username'], password=request.POSt['password1'])
            auth.login(request.user)
            return redirect('')
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request.user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'ID 또는 비밀번호가 일치하지 않습니다.'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
    return render(request,'login.html')
     