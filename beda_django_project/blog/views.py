from django.shortcuts import render

def index(request):
    return render(request, "beda/index.html")
    
def photo(request):
    return render(request, "beda/photo.html")

def contact(request):
    return render(request, "beda/contact.html")