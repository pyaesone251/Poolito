from django.shortcuts import render
from .models import *

# Create your views here.
def indexview(request):
    hero_area = HeroAera.objects.all().order_by('-id')[:1]
    contex = {
        'hero_area':hero_area
    }
    return render(request, 'index.html',contex)
