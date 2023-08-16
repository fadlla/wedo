from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('testimony', views.testimony, name='testimony'),
    path('contact', views.contact, name='contact'),
    path('save_testimonial/', views.save_testimonial, name='save_testimonial'),


]
