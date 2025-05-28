from django.urls import path
from .import views

urlpatterns = [
    path('',views.indexview, name='home'),
    path('about/',views.About_view, name='about'),
    path('service/',views.service_view,name='service'),
    path('blog/',views.blog_view,name='blgo'),
    path('contact/',views.contact_view, name='conatct'),
    path('team/',views.team_view, name='team'),
]
