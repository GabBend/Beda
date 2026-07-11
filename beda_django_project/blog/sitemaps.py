from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            "index",
            "zakazkova_vyroba",
            "plachty_na_miru",
            "autostany",
            "pergoly_a_pristresky",
            "teepee_a_taborove_vyrobky",
            "atypicke_vyrobky",
            "opravy_technickych_textilii",
            "photo",
            "contact",
        ]

    def location(self, item):
        return reverse(item)
