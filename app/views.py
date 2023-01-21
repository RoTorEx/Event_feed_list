from typing import Any

from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Achievement, Post, User
from .serializers import AchievementSerializer, PostSerializer, UserSerializer
from .utilities import get_advertising


class UserDetailView(APIView):
    """Output the user's feed on a get request with the user id in the request
    the feed will display the user himself, his notes and achievements, events are sorted
    by the time of creation, all advertisements are displayed."""

    def get(self, request: Request, pk: int) -> Response:
        user = User.objects.get(id=pk)
        return Response(
            {
                "user": UserSerializer(user).data,  # Output users's neews feed
                "advertisings": get_advertising(),  # Output neews feed
            }
        )


class PostListView(ListAPIView):
    """Output a list of posts for the user with the id passed in the get request"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self) -> Any:
        """Override get_queryset to filter by user id."""

        post = Post.objects.filter(user_id=self.kwargs.get("pk")).order_by("-date_create")
        return post

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Override to add ad output."""

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(
                {"posts": serializer.data, "advertisings": get_advertising()}  # Output ad list
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response({"posts": serializer.data, "advertisings": get_advertising()})  # Output ad list


class PostDetailView(APIView):
    """The conclusion of the post for the heading."""

    def get(self, request: Request, pk: int, title: str) -> Response:
        post = Post.objects.filter(user_id=pk, title=title)
        return Response(
            {"post": PostSerializer(post, many=True).data, "advertisings": get_advertising()}  # Output ad list
        )


class AchievementListView(APIView):
    """Output a list of achievements for the user."""

    def get(self, request: Request, pk: int) -> Response:
        achievement = Achievement.objects.filter(user_id=pk)
        return Response(
            {
                "achievements": AchievementSerializer(achievement, many=True).data,
                "advertisings": get_advertising(),  # Output ad list
            }
        )
