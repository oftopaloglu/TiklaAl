from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .forms import LoginForm

def index(request):
    return render(request, "index.html")

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Şifre sorunlu")
            return render(request,"login.html",context)

        messages.success(request,"Hoşgeldiniz")
        login(request,user)
        return redirect("pay")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış Yapıldı")
    return redirect("index")