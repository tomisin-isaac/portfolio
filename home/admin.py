from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

class SettingAdmin(admin.ModelAdmin):
    list_display = ('id','title','keywords','description','company')
    list_filter =('status',)
    list_display_links = ('id',)

class AboutAdmin(admin.ModelAdmin):
    list_display=('id', 'image','text')
    list_display_links = ('id',)

class QuestionsAdmin(admin.ModelAdmin):
    list_display=('id', 'image')
    list_display_links = ('id',)

class TestimoniesAdmin(admin.ModelAdmin):
    list_display = ('id','name','testimony','image')
    list_display_links = ('id',)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email','message','status','note')
    readonly_fields = ('name','email','message')
    list_filter = ['status']
    list_display_links = ('id',)
    search_fields = ('name','email','message','status','note')
    list_per_page = 20

class PortfolioAdmin(admin.ModelAdmin):
    list_display =['id','title','status','image']
    list_filter = ['status']
    prepopulated_fields ={'slug':('title',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','portfolio','status','image','slug']
    list_filter = ['portfolio']
    list_display_links = ('title','portfolio','status','image')
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug':('title',)}
# Register your models here.

admin.site.register(Setting,SettingAdmin)
admin.site.register(Team)
admin.site.register(About,AboutAdmin)
admin.site.register(Questions,QuestionsAdmin)
admin.site.register(Testimonies,TestimoniesAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)
admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(Product,ProductAdmin)
