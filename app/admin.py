from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Achievement, Advertising, Post, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date_create", "user")
    ordering = ("-date_create",)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "condition", "user", "icon")
    ordering = ("title",)

    def icon(self, obj):
        """Small icon in admin."""
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))

        return "Image not found"


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "date_create", "icon")
    ordering = ("-date_create",)

    def icon(self, obj):
        """Small icon in admin."""
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))

        return "Image not found"
