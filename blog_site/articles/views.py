from django.shortcuts import render

from .models import Maqola

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

# Create your views here.
