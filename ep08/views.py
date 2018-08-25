from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorUpdateOrReadonly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorUpdateOrReadonly]

    def perform_create(self, serializer):
        serializer.save(
                                ip=self.request.META['REMOTE_ADDR'],
                                author=self.request.user)