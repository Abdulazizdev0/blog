from django.shortcuts import render

from .models import *

def maqola(request):

    maqolalar = Maqola.objects.all().order_by('-id')
    context = {
        'maqolalar':maqolalar
    }
    return render(
        request=request,
        template_name='maqola.html',
        context = context
    
    )

def world_news(request):
    w_news = Maqola.objects.filter(tag='world').order_by('-id')
    print(w_news)
    context = {
        'w_news':w_news
    }
    return render(
        request=request,
        template_name='world.html',
        context=context
    )

def local_news(request):
    l_news = Maqola.objects.filter(tag='local').order_by('-id')
    context = {
        'l_news': l_news
    }
    return render(
        request=request,
        template_name='local.html',
        context = context
    )

def sport_news(request):
    s_news = Maqola.objects.filter(tag='sport').order_by('-id')
    print(s_news)
    context = {
        's_news': s_news
    }
    return render(
        request=request,
        template_name='sport.html',
        context = context
    )

# Create your views here.
