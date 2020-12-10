from rest_framework import serializers
from blog.post.models import Post
from blog.comment.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, min_length=1)
    author = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "created", "author", "comments"]
