from django.urls import include, path
from rest_framework import routers

from .views import AchievementViewSet, AdvertisingViewSet, FeedViewSet, PostViewSet, UserViewSet


router = routers.DefaultRouter()

router.register(r"users", UserViewSet)
router.register(r"posts", PostViewSet)
router.register(r"achievements", AchievementViewSet)
router.register(r"ads", AdvertisingViewSet)
router.register(r"feed", FeedViewSet, basename="feed")


urlpatterns = [
    path("", include(router.urls)),
    path("feed/<int:user_id>/", FeedViewSet.as_view({"get": "list"}), name="feed"),
]
