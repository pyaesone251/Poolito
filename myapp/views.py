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

def portfolio_view(request):
    return render(request,'portfolio.html')

def team_details_view(request):
    return render(request, 'team-details.html')

def service_details_view(request):
    return render(request, 'service-details.html')

def blog_details_view(request):
    return render(request,'blog-details.html')

def portfolio_details_view(request):
    return render(request,'portfolio-details.html')
