from rest_framework import viewsets, permissions
from blog.post.models import Post
from blog.post.serializers import PostSerializer
from blog.post.permissions import IsOwnerOrReadOnly


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
