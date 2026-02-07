from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("foto/", views.photo, name="photo"),
    path("kontakt/", views.contact, name="contact"),
]
