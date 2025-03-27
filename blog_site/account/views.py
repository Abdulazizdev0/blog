from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
from account.models import CustomUser


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        ex_user = CustomUser.objects.filter(email=email).first()
        if ex_user:
            return HttpResponse('<h1>Bu email orqali oldin royhatdan otilgan</h1>')
        elif password1 != password2:
            return HttpResponse('<h1>Parollarni togri kiriting </h1>')
        else:
            user = CustomUser(
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.set_password(password1)
            user.save()
            login(request=request,user=user)
            return redirect('maqola')


    return render(
        request=request,
        template_name='auth/register.html'
    )

def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        user = authenticate(email=email,password=password)
        print(user)
        if user:
            login(request=request, user=user)
            return redirect('maqola')
        else:
            return redirect('login')
    return render(
        request=request,
        template_name='auth/login.html'

    )

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('maqola')