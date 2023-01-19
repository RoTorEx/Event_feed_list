from rest_framework import serializers

from .models import Achievement, Advertising, Post, User


class PostSerializer(serializers.ModelSerializer):
    """Post serializer."""

    class Meta:
        model = Post
        fields = ("title", "date_create", "content")


class AchievementSerializer(serializers.ModelSerializer):
    """Achievement serializer."""

    class Meta:
        model = Achievement
        fields = ("title", "condition", "image")


class UserSerializer(serializers.ModelSerializer):
    """Nested user serializer with all events."""

    post = PostSerializer(many=True)
    achievement = AchievementSerializer(many=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "post", "achievement")


class AdvertisingSerializer(serializers.ModelSerializer):
    """Advertising serializer."""

    class Meta:
        model = Advertising
        fields = "__all__"  # ('title', 'content', 'image', 'url', 'date_create')
