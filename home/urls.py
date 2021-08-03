from django import urls
from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name=('index')),
    path('service/',views.service,name='service'),
    path('product/<str:id>/<slug:slug>',views.product_list,name='product_list'),
]
