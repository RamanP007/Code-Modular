from django.urls import path
from . import views
from django.contrib import admin

# Django admin header customization

admin.site.site_header = "Code Modular"
admin.site.site_title = "Welcome to Code Modular's Dashboard"
admin.site.index_title = "Welcome to Code Modular"


urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('projects/', views.projects, name = 'projects'),
    path('contact/', views.contact, name = 'contact'),
    
]