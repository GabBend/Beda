from django.shortcuts import render
from django.views.decorators.cache import cache_page

CACHE_30_DAYS = 60 * 60 * 24 * 30


@cache_page(CACHE_30_DAYS)
def index(request):
    return render(request, "beda/index.html")


@cache_page(CACHE_30_DAYS)
def zakazkova_vyroba(request):
    return render(request, "beda/zakazkova_vyroba.html")


@cache_page(CACHE_30_DAYS)
def plachty_na_miru(request):
    return render(request, "beda/plachty_na_miru.html")


@cache_page(CACHE_30_DAYS)
def autostany(request):
    return render(request, "beda/autostany_na_miru.html")


@cache_page(CACHE_30_DAYS)
def pergoly_a_pristresky(request):
    return render(request, "beda/pergoly_a_pristresky.html")


@cache_page(CACHE_30_DAYS)
def teepee_a_taborove_vyrobky(request):
    return render(request, "beda/teepee_a_taborove_vyrobky.html")


@cache_page(CACHE_30_DAYS)
def atypicke_vyrobky(request):
    return render(request, "beda/atypicke_vyrobky.html")


@cache_page(CACHE_30_DAYS)
def opravy_technickych_textilii(request):
    return render(request, "beda/opravy_technickych_textilii.html")


@cache_page(CACHE_30_DAYS)
def photo(request):
    return render(request, "beda/photo.html")


@cache_page(CACHE_30_DAYS)
def contact(request):
    return render(request, "beda/contact.html")
