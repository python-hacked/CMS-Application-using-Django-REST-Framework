from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import User, Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer
from .permissions import IsOwnerOrReadOnly


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]  
    lookup_field = "post_id"

    def perform_create(self, serializer):
        serializer.save()


    @action(detail=True, methods=["GET"])
    def likes(self, request, post_id=None):
        post = self.get_object()
        likes = Like.objects.filter(post=post)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)

        posts_with_likes = []
        for post_data in serializer.data:
            post = get_object_or_404(Post, post_id=post_data["post_id"])
            likes_count = Like.objects.filter(post=post).count()
            post_data["likes_count"] = likes_count
            posts_with_likes.append(post_data)

        return Response(posts_with_likes)

    def get_authenticated_user(self):
        if hasattr(self.request, "user") and self.request.user.is_authenticated:
            return self.request.user
        return None


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
