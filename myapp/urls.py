from django.urls import path
from .import views

urlpatterns = [
    path('',views.indexview, name='home'),
    path('about/',views.About_view, name='about'),
    path('service/',views.service_view,name='service'),
    path('blog/',views.blog_view,name='blgo'),
    path('contact/',views.contact_view, name='conatct'),
    path('team/',views.team_view, name='team'),
    path('portfolio/',views.portfolio_view, name='portfolio'),
    path('team-details/',views.team_details_view, name='team-details'),
    path('service-details/',views.service_details_view, name='service-details'),
    path('blog-details/',views.blog_details_view, name='blog-details'),
    path('portfolio-details/',views.portfolio_details_view, name='portfolio-details'),
]
