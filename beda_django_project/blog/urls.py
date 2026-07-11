from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "zakazkova-vyroba/",
        views.zakazkova_vyroba,
        name="zakazkova_vyroba",
    ),
    path(
        "plachty-na-miru/",
        views.plachty_na_miru,
        name="plachty_na_miru",
    ),
    path(
        "autostany-na-miru/",
        views.autostany,
        name="autostany",
    ),
    path(
        "pergoly-a-pristresky/",
        views.pergoly_a_pristresky,
        name="pergoly_a_pristresky",
    ),
    path(
        "teepee-a-taborove-vyrobky/",
        views.teepee_a_taborove_vyrobky,
        name="teepee_a_taborove_vyrobky",
    ),
    path(
        "atypicke-vyrobky/",
        views.atypicke_vyrobky,
        name="atypicke_vyrobky",
    ),
    path(
        "opravy-technickych-textilii/",
        views.opravy_technickych_textilii,
        name="opravy_technickych_textilii",
    ),
    path("foto/", views.photo, name="photo"),
    path("kontakt/", views.contact, name="contact"),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain",
        ),
    ),
]
