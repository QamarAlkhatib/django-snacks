from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
# rendring HTML pages
#class based views, another way-> function based views

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about-us.html'
