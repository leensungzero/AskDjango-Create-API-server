from django.shortcuts import render
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

post_list = PostViewSet.as_view({
    'get': 'list',
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
})