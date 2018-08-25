from ep04.models import Post
from rest_framework.viewsets import ModelViewSet
from ep04.serializers import PostSerializer
from rest_framework.filters import SearchFilter

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

    '''
    def get_queryset(self):
        qs = super().get_queryset()

        # search = self.request.GET.get('search', '')
        # if search:
        #     qs = qs.filter(title__icontains=search)

        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs
    '''