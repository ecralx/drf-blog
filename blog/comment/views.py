from rest_framework import viewsets, permissions
from blog.comment.models import Comment
from blog.comment.serializers import CommentSerializer
from blog.utils.permissions import IsOwnerOrReadOnly


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
