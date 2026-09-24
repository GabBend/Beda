from datetime import timedelta

from django.db.models import F, Sum
from django.shortcuts import render
from django.utils import timezone

from .models import NavstevaWebu


def zapocitat_navstevu(request):
    dnes = timezone.localdate()
    klic_navstevy = f"navsteva_webu_{dnes.isoformat()}"

    # Nezapočítáváme stejný prohlížeč vícekrát během jednoho dne
    if request.session.get(klic_navstevy):
        return

    # Jednoduché odfiltrování vyhledávačů a robotů
    user_agent = request.META.get("HTTP_USER_AGENT", "").lower()
    roboti = ("bot", "crawler", "spider", "slurp", "bingpreview")

    if any(robot in user_agent for robot in roboti):
        return

    navsteva, _ = NavstevaWebu.objects.get_or_create(
        datum=dnes,
        defaults={"pocet": 0},
    )

    NavstevaWebu.objects.filter(pk=navsteva.pk).update(pocet=F("pocet") + 1)

    request.session[klic_navstevy] = True


def index(request):
    zapocitat_navstevu(request)
    return render(request, "beda/index.html")


def zakazkova_vyroba(request):
    zapocitat_navstevu(request)
    return render(request, "beda/zakazkova_vyroba.html")


def plachty_na_miru(request):
    zapocitat_navstevu(request)
    return render(request, "beda/plachty_na_miru.html")


def autostany(request):
    zapocitat_navstevu(request)
    return render(request, "beda/autostany_na_miru.html")


def pergoly_a_pristresky(request):
    zapocitat_navstevu(request)
    return render(request, "beda/pergoly_a_pristresky.html")


def teepee_a_taborove_vyrobky(request):
    zapocitat_navstevu(request)
    return render(request, "beda/teepee_a_taborove_vyrobky.html")


def atypicke_vyrobky(request):
    zapocitat_navstevu(request)
    return render(request, "beda/atypicke_vyrobky.html")


def opravy_technickych_textilii(request):
    zapocitat_navstevu(request)
    return render(request, "beda/opravy_technickych_textilii.html")


def photo(request):
    zapocitat_navstevu(request)
    return render(request, "beda/photo.html")


def contact(request):
    zapocitat_navstevu(request)

    dnes = timezone.localdate()
    pred_7_dny = dnes - timedelta(days=6)
    pred_30_dny = dnes - timedelta(days=29)

    navstevy_dnes = (
        NavstevaWebu.objects.filter(datum=dnes).values_list("pocet", flat=True).first()
        or 0
    )

    navstevy_7_dni = (
        NavstevaWebu.objects.filter(datum__gte=pred_7_dny).aggregate(
            celkem=Sum("pocet")
        )["celkem"]
        or 0
    )

    navstevy_30_dni = (
        NavstevaWebu.objects.filter(datum__gte=pred_30_dny).aggregate(
            celkem=Sum("pocet")
        )["celkem"]
        or 0
    )

    navstevy_celkem = NavstevaWebu.objects.aggregate(celkem=Sum("pocet"))["celkem"] or 0

    context = {
        "navstevy_dnes": navstevy_dnes,
        "navstevy_7_dni": navstevy_7_dni,
        "navstevy_30_dni": navstevy_30_dni,
        "navstevy_celkem": navstevy_celkem,
    }

    return render(request, "beda/contact.html", context)
