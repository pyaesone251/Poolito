from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Heroaera(models.Model):
    icon_bg = models.ImageField(upload_to='hero_aera',null=True,blank=True)
    icon_title = models.CharField(max_length=200,null=True,blank=True)
    bg_img = models.ImageField(upload_to='hero_aera',null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    note = models.CharField(max_length=200,null=True,blank=True)
    video = models.URLField(null=True,blank=True)

class Service1(models.Model):
    title = RichTextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    icon = models.ImageField(upload_to='service1',null=True,blank=True)
    background_img = models.ImageField(upload_to='service1',null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery',null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)

class Cleaning_Service(models.Model):
    title = RichTextField(null=True,blank=True)
    descriptions = models.TextField(null=True,blank=True)
    img = models.ImageField(upload_to='cleaning_service',null=True,blank=True)
    icon_img = models.ImageField(upload_to='cleaning_service',null=True,blank=True)
    title1 = models.CharField(max_length=100,null=True,blank=True)
    note = models.TextField(null=True,blank=True)

class Review_left(models.Model):
    name = RichTextField(null=True,blank=True)
    image = models.ImageField(upload_to='review_left',null=True,blank=True)
    video = models.URLField(null=True,blank=True)

class Review_title(models.Model):
    name = RichTextField(null=True,blank=True)
    title = RichTextField(null=True,blank=True)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now_add=True)

class Review(models.Model):
    name = RichTextField(null=True,blank=True)
    review = RichTextField(null=True,blank=True)
    image = models.ImageField(upload_to='review',null=True,blank=True)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now_add=True)

class Counter(models.Model):
    icon_img = models.ImageField(upload_to='counter',null=True,blank=True)
    name  = RichTextField(null=True,blank=True)
    count = RichTextField(null=True,blank=True)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now_add=True)

class Cleaning_service1(models.Model):
    img = models.ImageField(upload_to='cleaning_service',null=True,blank=True)
    icon_img = models.ImageField(upload_to='cleaning_service',null=True,blank=True)
    title1 = models.CharField(max_length=100,null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now_add=True)
