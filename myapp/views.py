from django.shortcuts import render
from .models import * 

# Create your views here.
def indexview(request):
    hero_aera = Heroaera.objects.all().order_by('-id')[:1]
    service1 = Service1.objects.all().order_by('id')[:4]
    gallery = Gallery.objects.all().order_by('id')[:8]
    cleaning_service = Cleaning_Service.objects.all().order_by('id')[:1]
    review_left = Review_left.objects.all().order_by('id')[:1]
    review_title = Review_title.objects.all()
    review = Review.objects.all()
    counter = Counter.objects.all().order_by('id')[:4]
    cleaning_service1 = Cleaning_service1.objects.all().order_by('id')[:5]
    contex = {
        'hero_aera':hero_aera,
        'service1':service1,
        'gallery':gallery,
        'cleaning_service':cleaning_service,
        'review_left' : review_left,
        'review_title' :review_title,
        'review':review,
        'counter':counter,
        'cleaning_service1':cleaning_service1
    }
    return render(request,'index.html',contex)
def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def service_details(request):
    return render(request,'service-details.html')

def blog(request):
    return render(request,'blog.html')

def blog_details(request):
    return render(request,'blog-details.html')

def team(request):
    return render(request,'team.html')

def team_details(request):
    return render(request,'team-details.html')

def contact(request):
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')

def portfolio_details(request):
    return render(request,'portfolio-details.html')