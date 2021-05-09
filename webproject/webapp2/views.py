import auth as auth
from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.
def log(request):
    if request.method == "POST":
        u = request.POST['usname']
        p = request.POST['password']
        user = auth.authenticate(username=u,password=p)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credential')
            return redirect('log')
    return render(request,'login.html')
def reg(request):
    if request.method == "POST":
        un = request.POST['uname']
        fn = request.POST['First_name']
        sn = request.POST['Second_name']
        em = request.POST['email']
        pw1 = request.POST['password1']
        pw2 = request.POST['password2']
        if pw1 == pw2:
            if User.objects.filter(username=un).exists():
                messages.info(request,"Username Already Exit")
                return redirect('reg')
            elif User.objects.filter(email=em).exists():
                messages.info(request,"Email Already Exit")
                return  redirect('reg')
            else:
                user = User.objects.create_user(username=un,first_name=fn,last_name=sn,email=em,
                                        password=pw1)
                user.save();
                return redirect('log')
                print("User Created")
        else:
            messages.info(request,"Password not matching")
            return redirect('reg')
        return redirect('/')
    return render(request,'register.html')
#logout
def out(request):
    auth.logout(request)
    return redirect('/')

