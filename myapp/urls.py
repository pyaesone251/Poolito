from django.urls import path
from .import views

urlpatterns = [
    path('',views.indexview, name='home'),
    path('about/',views.about, name='about'),
    path('service/',views.service, name='service'),
    path('service-details/',views.service_details, name='service-details'),
    path('blog/',views.blog, name='blog'),
    path('blog-details/',views.blog_details, name='blog-details'),
    path('team/',views.team, name='team'),
    path('team-details/',views.team_details, name='team-details'),
    path('contact/',views.contact, name='contact'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('portfolio-details/',views.portfolio_details, name='portfolio-details'),
]