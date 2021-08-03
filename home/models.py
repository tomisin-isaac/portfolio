from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.forms import Textarea, TextInput
from django.forms import ModelForm
# from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Setting(models.Model):
    STATUS =(
        ('True','True'),
        ('False','False'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, blank=True)
    icon = models.ImageField(blank=True, null=True, upload_to='images/')
    logo = models.ImageField(blank=True, null=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=100)
    instargram = models.CharField(blank=True, max_length=100)
    twitter = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS)

    def __str__(self):
        return self.title

class Team(models.Model):
    team_img = models.ImageField(upload_to='images/',blank=True, null=True)
    team_name = models.CharField(max_length=30, default="Tomisin Isaac")
    team_job = models.CharField(max_length=30, default='WEB DEVELOPER')

    def __str__(self):
        return self.team_name

class About(models.Model):
    text = models.CharField(max_length=900, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to= 'images/')


class Questions(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to= 'images/')
    map = models.ImageField(blank=True, null=True, upload_to='images/')

class Testimonies(models.Model):
    name = models.CharField(blank=True, null=True, max_length=200)
    testimony = models.CharField(blank=True, null=True, max_length=900)
    image = models.ImageField(blank=True, null=True, upload_to='images/')


class ContactMessage(models.Model):
    STATUS =(
        ('New','New'),
        ('Read','Read'),
        ('pending','pending'),
        ('Closed','Closed'),
    )

    name = models.CharField(blank=True,max_length=20)
    email = models.CharField(blank=True, max_length=50)
    message = models.CharField(blank=True, max_length=225)
    status = models.CharField(choices=STATUS, default='New', max_length=10)
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.name
    

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','message']   


class Portfolio(models.Model):
    STATUS =(
        ('True','True'),
        ('False','False'),
    )
    title = models.CharField(max_length=150)
    title2 = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("catetory_details", kwargs={"slug": self.slug})

class Product(models.Model):
    STATUS=(
        ('True','True'),
        ('False','False'),
    )
    portfolio = models.ForeignKey(Portfolio, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150, blank=True,)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    details = models.CharField(blank=True, null=True, max_length=900)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    reviewimg = models.ImageField(blank=True, null=True, upload_to='images')
    name = models.CharField(blank=True, null=True, max_length=30)
    date = models.CharField(blank=True, null=True, max_length=20)
    review  = models.CharField(blank=True, null=True, max_length=900)
    reviewimg2 = models.ImageField(blank=True, null=True, upload_to='images')
    name2 = models.CharField(blank=True, null=True, max_length=30)
    date2 = models.CharField(blank=True, null=True, max_length=20)
    review2  = models.CharField(blank=True, null=True, max_length=900)

    
    def __str__(self):
        return self.title
    

    def image_tag(self):
        return mark_safe('<img src="()" height="50px"/>'.format(self.image.url))

    image_tag.short_description = 'image'

    def get_absolute_url(self):
        return reverse("category_details", kwargs={"slug": self.slug})