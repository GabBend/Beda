from django.shortcuts import render
from django.views.decorators.cache import cache_page

cache_page(60*60*24*30) 
def index(request):
    return render(request, "beda/index.html")

cache_page(60*60*24*30) 
def photo(request):
    return render(request, "beda/photo.html")

cache_page(60*60*24*30) 
def contact(request):
    return render(request, "beda/contact.html")