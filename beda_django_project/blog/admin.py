from django.contrib import admin

from .models import NavstevaWebu, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(NavstevaWebu)
class NavstevaWebuAdmin(admin.ModelAdmin):
    list_display = ("datum", "pocet")
    ordering = ("-datum",)
    readonly_fields = ("datum", "pocet")
