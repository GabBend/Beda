from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]

if settings.DEBUG and getattr(settings, "DEBUG_TOOLBAR", False):
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
