from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Achievement, Advertising, Post, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created", "user")
    ordering = ("-date_created",)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("name", "conditions", "user", "icon")
    ordering = ("name",)

    def icon(self, obj):
        """Small icon in admin."""
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))

        return "Image not found"


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "date_created", "icon")
    ordering = ("-date_created",)

    def icon(self, obj):
        """Small icon in admin."""
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))

        return "Image not found"
