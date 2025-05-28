from django.shortcuts import render
from .models import *

# Create your views here.
def indexview(request):
    hero_area = HeroAera.objects.all().order_by('-id')[:1]
    contex = {
        'hero_area':hero_area
    }
    return render(request, 'index.html',contex)

def About_view(request):
    return render(request, 'about.html')

def service_view(request):
    return render(request,'service.html')

def blog_view(request):
    return render(request, 'blog.html')

def contact_view(request):
    return render(request, 'contact.html')

def team_view(request):
    return render(request, 'team.html')
