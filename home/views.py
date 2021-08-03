from home.models import About, ContactForm, Portfolio, Product, Questions, Setting, Team, Testimonies
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message has been sent! our customer serverce Team would be with you shortly')
            return redirect('index')

    setting = Setting.objects.get(pk=1)
    team = Team.objects.all()
    about = About.objects.get(pk=1)
    questions = Questions.objects.get(pk=1)
    testimony = Testimonies.objects.all()
    form = ContactForm
    portfolio = Portfolio.objects.all()
    context={
        'setting':setting,
        'team':team,
        'about':about,
        'questions':questions,
        'testimony': testimony,
        'form':form,
        'portfolio':portfolio,
    }
    return render(request, 'index.html',context)

def product_list(request,id,slug):
    setting = Setting.objects.get(pk=1)
    team = Team.objects.all()
    about = About.objects.get(pk=1)
    questions = Questions.objects.get(pk=1)
    testimony = Testimonies.objects.all()
    portfolio = Portfolio.objects.all()
    product = Product.objects.all()[:1]
    products = Product.objects.get(pk=1)
    context={
        'setting':setting,
        'team':team,
        'about':about,
        'questions':questions,
        'testimony': testimony,
        'portfolio':portfolio,
        'product':product,
        'products':products
    }
    return render(request,'product.html',context)

def service(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message has been sent! our customer serverce Team would be with you shortly')
            return redirect('index')

    setting = Setting.objects.get(pk=1)
    team = Team.objects.all()
    about = About.objects.get(pk=1)
    questions = Questions.objects.get(pk=1)
    testimony = Testimonies.objects.all()
    form = ContactForm
    portfolio = Portfolio.objects.all()
    context={
        'setting':setting,
        'team':team,
        'about':about,
        'questions':questions,
        'testimony': testimony,
        'form':form,
        'portfolio':portfolio,
    }
    return render(request, 'servicepage.html',context)
