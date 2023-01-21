from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Achievement, Advertising, Post, User
from .serializers import AchievementSerializer, AdvertisingSerializer, PostSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """View return list of all users."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["first_name", "last_name"]


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """View return list of all posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "body"]
    ordering_fields = ["date_created"]


class AchievementViewSet(viewsets.ReadOnlyModelViewSet):
    """View return list of all achievement."""

    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "user"]


class AdvertisingViewSet(viewsets.ReadOnlyModelViewSet):
    """View return list of all advertisements."""

    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["date_published"]


class FeedViewSet(viewsets.ViewSet):
    """Main view of feed list."""

    pagination_class = PageNumberPagination

    def list(self, request, user_id=None):
        posts = Post.objects.filter(user_id=user_id)
        posts_serializer = PostSerializer(posts, many=True)
        achievements = Achievement.objects.filter(user_id=user_id)
        achievements_serializer = AchievementSerializer(achievements, many=True)
        ads = Advertising.objects.all()
        ads_serializer = AdvertisingSerializer(ads, many=True)
        event_type = self.request.query_params.get('event_type', None)

        match event_type:
            case "post":
                return Response(posts_serializer.data)

            case 'achievement':
                return Response(achievements_serializer.data)

            case "advertising":
                return Response(ads_serializer.data)

            case _:
                return Response(
                    {
                        "posts": posts_serializer.data,
                        "achievements": achievements_serializer.data,
                        "advertising": ads_serializer.data,
                    }
                )
