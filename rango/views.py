from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page
# Create your views here.

def show_category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {
        'categories': category_list,
        'pages': pages_list,
    }
    ##topfivelist = []

    ##for pages in Page.objects.all():
    ##    for i in range(0,5):
    ##        if pages.topfivelist[i]




    return render(request, 'rango/index.html', context=context_dict)

    ##return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")
def about(request):
    context_dict = {'aboutmessage': "Created by Domenico Restuccia UofG 2201547",}

    return render(request, 'rango/about.html', context=context_dict)

    ##return HttpResponse("Rango says this is the about Page <br/> Created by Domenico Restuccia UofG 2201547 <br/> <a href='/rango/index/'>Index</a>")

