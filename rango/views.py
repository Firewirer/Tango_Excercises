from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

def about(request):
	return HttpResponse("Rango says this is the about Page <br/> Created by Domenico Restuccia UofG 2201547 <br/> <a href='/rango/index/'>Index</a>")

