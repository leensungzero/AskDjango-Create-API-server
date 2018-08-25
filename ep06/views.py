from ep04.models import Post
from rest_framework.viewsets import ModelViewSet
from ep04.serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer