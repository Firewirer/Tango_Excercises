from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, cangy, cupcake!"}

    return render(request, 'rango/index.html', context=context_dict)

    ##return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")
def about(request):
    context_dict = {'aboutmessage': "Created by Domenico Restuccia UofG 2201547",}

    return render(request, 'rango/about.html', context=context_dict)

    ##return HttpResponse("Rango says this is the about Page <br/> Created by Domenico Restuccia UofG 2201547 <br/> <a href='/rango/index/'>Index</a>")

