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
    blog = Blog.objects.all().order_by('id')[:4]
    blogcategory = BlogCategory.objects.all().order_by('id')[:2]
    footer_gallery = Footer_gallery.objects.all().order_by('-id')[:6]
    contex = {
        'hero_aera':hero_aera,
        'service1':service1,
        'gallery':gallery,
        'cleaning_service':cleaning_service,
        'review_left' : review_left,
        'review_title' :review_title,
        'review':review,
        'counter':counter,
        'cleaning_service1':cleaning_service1,
        'blog':blog,
        'blogcategory':blogcategory,
        'footer_gallery':footer_gallery,
    }
    return render(request,'index.html',contex)

def about(request):
    footer_gallery = Footer_gallery.objects.all().order_by('-id')[:6]
    contex = {
        'footer_gallery':footer_gallery,
    }
    return render(request,'about.html',contex)

def service(request):
    footer_gallery = Footer_gallery.objects.all().order_by('-id')[:6]
    contex = {
        'footer_gallery':footer_gallery,
    }
    return render(request,'service.html',contex)

def service_details(request):
    footer_gallery = Footer_gallery.objects.all().order_by('-id')[:6]
    contex = {
        'footer_gallery':footer_gallery,
    }
    return render(request,'service-details.html',contex)

def blog(request):
    footer_gallery = Footer_gallery.objects.all().order_by('-id')[:6]
    contex = {
        'footer_gallery':footer_gallery,
    }
    return render(request,'blog.html',contex)

def blog_details(request):
    footer_gallery = Footer_gallery.objects.all().order_by('-id')[:6]
    contex = {
        'footer_gallery':footer_gallery,
    }
    return render(request,'blog-details.html',contex)

def team(request):
    teamaera = Teamaera.objects.all().order_by('id')[:8]
    footer_gallery = Footer_gallery.objects.all().order_by('-id')[:6]
    contex ={
        'teamaera':teamaera,
        'footer_gallery':footer_gallery,
    }
    return render(request,'team.html',contex)

def team_details(request):
    team_details = Team_details.objects.all()
    footer_gallery = Footer_gallery.objects.all().order_by('-id')[:6]
    contex = {
        'team_details':team_details,
        'footer_gallery':footer_gallery,
    }
    return render(request,'team-details.html',contex)

def contact(request):
    footer_gllery = Footer_gallery.objects.all().order_by('-id')[:6]
    contex = {
        'footer_gallery':footer_gllery,
    }
    return render(request,'contact.html',contex)

def portfolio(request):
    footer_gallery = Footer_gallery.objects.all().order_by('-id')[:6]
    contex = {
        'footer_gallery':footer_gallery,
    }
    return render(request,'portfolio.html',contex)

def portfolio_details(request):
    footer_gallery = Footer_gallery.objects.all().order_by('-id')[:6]
    contex = {
        'footer_gallery':footer_gallery,
    }
    return render(request,'portfolio-details.html',contex)
