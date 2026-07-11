from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import StaticViewSitemap
from django.views.generic import RedirectView
from django.templatetags.static import static

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("", include("blog.urls")),
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=static("favicon.ico"),
            permanent=True,
        ),
    ),
]

if settings.DEBUG and getattr(settings, "DEBUG_TOOLBAR", False):
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
